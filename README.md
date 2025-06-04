# Apple Documentation Scraper for Context7

A Python tool that scrapes and converts Apple's developer documentation into markdown format optimized for AI LLM and specifically for Context7 integration, enabling natural language queries across Apple's entire documentation ecosystem. The current Apple Documentation site requires Javascript and is not friendly to LLM's.

## 🚀 Apple JSON API

This project utilizes the JSON API endpoints that uses internally for all documentation pages. This eliminates the need for HTML parsing or browser automation.

## Purpose

This scraper addresses the need for offline, searchable access to Apple's developer documentation by:
- Converting Apple's documentation into clean, structured markdown files
- Organizing content for efficient retrieval via Context7
- Enabling queries like "apple swiftui list" or "apple metal shader"
- Preserving code examples, cross-references, and platform availability information

## Technical Approach

The scraper leverages Apple's JSON API endpoints that power their documentation viewer:
```
Documentation URL: https://developer.apple.com/documentation/swiftui/text.json
Pair JSON API URL: https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
```

This approach provides:
- **100x faster scraping** - Direct HTTP requests instead of browser automation
- **Complete structured data** - All content, code examples, and metadata in JSON format
- **Scalable to 100,000+ pages** - Simple async HTTP requests with rate limiting
- **Generic solution** - One scraper works for ALL frameworks
- **No JavaScript rendering needed** - Pure API calls

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd apple-doc-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

### Basic Commands

```bash
# Scrape a single page (test)
python -m scraper.main scrape-page swiftui https://developer.apple.com/documentation/swiftui/text

# Scrape an entire framework
python -m scraper.main scrape-framework watchkit

# Discovery mode - find all pages in a framework
python -m scraper.main discover watchkit
```

### Configuration

Don't spam Apple. All settings use optimized defaults. Optionally customize with environment variables:

```bash
# Optional performance tuning
export RATE_LIMIT_DELAY=0.2          # Seconds between requests (default: 0.2)
export MAX_CONCURRENT_REQUESTS=10     # Parallel requests (default: 10)
export OUTPUT_DIR=./documentation    # Output directory (default: ./documentation)
```

## Output Format

Documentation is saved as markdown files organized by framework:

```
documentation/
├── swiftui/
│   ├── text.md
│   ├── button.md
│   ├── view_frame(width:height:alignment:).md
│   └── declaring-a-custom-view.md
├── uikit/
│   ├── uiview.md
│   └── uiviewcontroller.md
└── metal/
    ├── mtldevice.md
    └── mtlcommandqueue.md
```

Each markdown file contains:
- API name and framework
- Platform availability
- Swift/Objective-C declarations
- Detailed descriptions
- Code examples
- Cross-references with dual linking (local .md files + Apple URLs)
- Link to original documentation

## Architecture

### Key Components

- **JSON Scraper** (`scraper/json_scraper.py`) - Fetches and parses Apple's JSON API
- **URL Discovery** - Traverses documentation graph to find all pages
- **Markdown Converter** - Transforms JSON to Context7-optimized markdown
- **Hash Manager** - Tracks changes for incremental updates
- **Rate Limiter** - Respects server limits with adaptive delays

### Supported Frameworks

The scraper handles all Apple frameworks including:
- All 150+ frameworks listed on developer.apple.com/documentation/

## Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=scraper

# Type checking
mypy scraper
```

## Troubleshooting

**Rate Limiting**: The scraper automatically handles rate limits with exponential backoff.

**Memory Usage**: For large-scale scraping, process frameworks in batches.

**Missing Content**: Some pages may not have JSON endpoints.

## License

MIT License - They're Apple's docs so do whatever you want with them.

## Acknowledgments

Built for Context7 integration to enable natural language access to Apple's developer documentation.