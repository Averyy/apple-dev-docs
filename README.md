# Apple Documentation Scraper for Context7

A Python tool that scrapes and converts Apple's developer documentation into markdown format optimized for Context7 integration, enabling natural language queries across Apple's entire documentation ecosystem.

## Purpose

This scraper addresses the need for offline, searchable access to Apple's developer documentation by:
- Converting Apple's documentation into clean, structured markdown files
- Organizing content for efficient retrieval via Context7
- Enabling queries like "apple swiftui list" or "apple metal shader"
- Preserving code examples, cross-references, and platform availability information

## Technical Approach

The scraper leverages Apple's JSON API endpoints that power their documentation viewer:
```
Documentation URL: https://developer.apple.com/documentation/swiftui/text
JSON API URL:     https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
```

This approach provides:
- Direct access to structured data (no HTML parsing required)
- Complete content including code examples and metadata
- Efficient scraping without browser automation
- Reliable data extraction at scale

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
# Quick test scraping (recommended first step)
python3 -c "
import asyncio
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.config import Config

async def test(): 
    Config.ensure_directories()
    scraper = AppleJSONDocumentationScraper('swiftui')
    async with scraper:
        data = await scraper.extract_page_data(None, 'https://developer.apple.com/documentation/swiftui/text')
        if data: await scraper.save_page_data('https://developer.apple.com/documentation/swiftui/text', data)
        print('✅ Test complete!')
asyncio.run(test())
"

# Full framework scraping (in development)
# python -m scraper scrape swiftui
```

### Configuration

All settings use optimized defaults. Optionally customize with environment variables:

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

### Example Output

```markdown
# Text

**Framework**: SwiftUI

A view that displays one or more lines of read-only text.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen struct Text
```

## Overview

A text view draws a string in your app's user interface...
```

## Architecture

### Key Components

- **JSON Scraper** (`scraper/json_scraper.py`) - Fetches and parses Apple's JSON API
- **URL Discovery** - Traverses documentation graph to find all pages
- **Markdown Converter** - Transforms JSON to Context7-optimized markdown
- **Hash Manager** - Tracks changes for incremental updates
- **Rate Limiter** - Respects server limits with adaptive delays

### Supported Frameworks

The scraper handles all Apple frameworks including:
- **UI**: SwiftUI, UIKit, AppKit
- **Graphics**: Metal, Core Graphics, Core Animation
- **Media**: AVFoundation, Core Audio, Core Image
- **System**: Foundation, Security, Network
- **ML/AI**: Core ML, Create ML, Natural Language
- And 150+ more frameworks

## Development

### Project Structure

```
apple-doc-scraper/
├── scraper/                 # Main package
│   ├── json_scraper.py     # Core scraping logic
│   ├── base.py            # Base classes
│   └── utils/             # Utilities
├── tests/                 # Test suite
├── documentation/         # Output directory
└── requirements.txt       # Dependencies
```

### Running Tests

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

**Missing Content**: Some pages may not have JSON endpoints (rare). These are logged for manual review.

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## Acknowledgments

Built for Context7 integration to enable natural language access to Apple's developer documentation.