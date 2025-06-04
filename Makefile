.PHONY: help install dev-install test lint type-check format clean run-swiftui analyze-swiftui

help:
	@echo "Available commands:"
	@echo "  make install        - Install production dependencies"
	@echo "  make dev-install    - Install all dependencies including dev tools"
	@echo "  make test          - Run test suite"
	@echo "  make lint          - Run linting (ruff)"
	@echo "  make type-check    - Run type checking (mypy)"
	@echo "  make format        - Format code with black"
	@echo "  make clean         - Clean cache and temporary files"
	@echo "  make run-swiftui   - Run SwiftUI scraper pilot"
	@echo "  make analyze-swiftui - Analyze SwiftUI docs structure with Puppeteer"

install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest -v

test-coverage:
	pytest --cov=scraper --cov-report=html --cov-report=term-missing

lint:
	ruff check scraper tests

type-check:
	mypy scraper

format:
	black scraper tests
	ruff check --fix scraper tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache
	rm -rf build dist *.egg-info

run-swiftui:
	python -m scraper.main --framework swiftui --log-level INFO

analyze-swiftui:
	python -m scraper.analyze --url https://developer.apple.com/documentation/swiftui

# Development shortcuts
check: lint type-check test
all: format check