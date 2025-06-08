# Getting Started with Apple Documentation Scraper

## 🎉 Great News: Apple Provides JSON APIs!

We've discovered that Apple provides JSON API endpoints for all their documentation pages. This means:
- No complex HTML parsing
- No browser automation needed
- Direct access to structured data
- 100x faster and more reliable

## Quick Start

### 1. Understanding the JSON API

Every Apple documentation page has a corresponding JSON endpoint:

```
Documentation: https://developer.apple.com/documentation/swiftui/text
JSON API:      https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
```

### 2. Basic Setup

```bash
# Clone the repository
git clone <repository-url>
cd apple-developer-docs

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (includes optimized settings)
pip install -e .
```

### 3. Test the Scraper

```python
# Test with individual pages (validated approach)
import asyncio
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.config import Config

async def test_scraper():
    Config.ensure_directories()
    scraper = AppleJSONDocumentationScraper('swiftui')
    
    async with scraper:
        # Test with SwiftUI Text API
        data = await scraper.extract_page_data(
            None, 
            'https://developer.apple.com/documentation/swiftui/text'
        )
        if data:
            await scraper.save_page_data(
                'https://developer.apple.com/documentation/swiftui/text', 
                data
            )
            print('✅ Test successful!')

asyncio.run(test_scraper())
```

### 4. Run Full Framework Scrape

```python
# Discover and scrape all SwiftUI documentation
urls = await scraper.discover_urls()
print(f"Found {len(urls)} documentation pages")

# Scrape all pages
await scraper.scrape_all()
```

## How It Works

1. **URL Discovery**: Starting from framework root, the scraper follows JSON references to discover all pages
2. **JSON Fetching**: Direct HTTP requests to JSON endpoints (no browser needed!)
3. **Data Extraction**: Parse structured JSON data including:
   - Title, description, availability
   - Code declarations and examples
   - Parameters and return values
   - Related topics and cross-references
4. **Markdown Generation**: Convert to clean, formatted markdown
5. **Storage**: Save to local filesystem mirroring Apple's structure

## Example Output

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

## Supported Frameworks

The scraper works with ALL Apple frameworks:
- SwiftUI
- UIKit
- Foundation
- Metal
- ARKit
- Core ML
- And 340+ more! (341 frameworks total)

## Performance (Production Ready)

With our production-tested JSON API approach:
- **Rate limiting**: 0.2s delays (5 pages/sec), adaptive down to 0.1s
- **Concurrent processing**: 10 parallel requests
- **SwiftUI**: ~5 minutes for 2,800+ pages
- **Full deployment**: 278,778 pages completed successfully
- **ETag optimization**: Incremental updates in ~30 minutes
- **Memory efficient**: Streaming processing with cleanup
- **No browser overhead**: Direct HTTP to JSON endpoints

## Next Steps

1. Choose frameworks to scrape
2. Configure rate limiting (be respectful!)
3. Run the scraper
4. Process markdown output for Context7

## Troubleshooting

### Rate Limiting
- Add delays between requests
- Use adaptive rate limiting
- Monitor for 429 responses

### Missing Content
- Check JSON endpoint exists
- Verify URL transformation
- Some pages may not have JSON (rare)

### Memory Usage
- Process in batches
- Clear cache periodically
- Use async generators for large datasets