from __future__ import unicode_literals

from django.apps import AppConfig


class CongressScraperConfig(AppConfig):
    name = 'congress_scraper'
    app.config.broker_url='redis://localhost:6379/0'
