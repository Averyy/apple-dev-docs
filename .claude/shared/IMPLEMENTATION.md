# Implementation Details: Apple JSON Documentation Scraper

## The JSON API Discovery

Apple's documentation system uses a hidden JSON API that powers their documentation viewer. Every documentation page has a corresponding JSON endpoint containing all the structured data.

### URL Pattern Transformation

```python
def convert_doc_url_to_json_url(doc_url: str) -> str:
    """Convert documentation URL to JSON API URL."""
    # From: https://developer.apple.com/documentation/swiftui/text
    # To:   https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
    
    return doc_url.replace(
        "/documentation/", 
        "/tutorials/data/documentation/"
    ) + ".json"
```

## JSON Structure Analysis

### Root Level Structure
```json
{
    "identifier": {...},
    "metadata": {
        "title": "Text",
        "role": "symbol",
        "modules": [{"name": "SwiftUI"}],
        "platforms": [...]
    },
    "abstract": [...],
    "primaryContentSections": [...],
    "topicSections": [...],
    "seeAlsoSections": [...],
    "references": {...}
}
```

### Key Data Fields

1. **Metadata** - Title, role, framework info
2. **Abstract** - Brief description (array of text objects)
3. **Platforms** - Availability info with versions
4. **Primary Content** - Main documentation content
   - Declarations
   - Overview/Discussion
   - Parameters
   - Return values
5. **Topic Sections** - Grouped related APIs
6. **References** - Link definitions for cross-references

## Implementation Architecture

### 1. Base Scraper Class
```python
class BaseAppleScraper:
    """Base class with common functionality."""
    - Rate limiting
    - HTTP client management
    - Progress tracking
    - Error handling
```

### 2. JSON Documentation Scraper
```python
class AppleJSONDocumentationScraper(BaseAppleScraper):
    """Generic scraper for all Apple frameworks."""
    
    async def discover_urls(self) -> List[str]:
        """Discover all docs by following JSON references."""
        
    async def extract_page_data(self, url: str) -> Dict:
        """Fetch JSON and extract structured data."""
        
    def _extract_from_json(self, json_data: Dict) -> Dict:
        """Parse JSON into our standard format."""
```

### 3. Markdown Converter
```python
class AppleDocMarkdownConverter:
    """Convert extracted data to markdown."""
    
    def convert_page(self, data: Dict) -> str:
        """Generate markdown from structured data."""
```

## URL Discovery Algorithm

```python
async def discover_urls(self):
    # 1. Start with framework root JSON
    root_url = f"{JSON_BASE}/framework_id.json"
    
    # 2. Extract all identifiers from:
    #    - topicSections
    #    - relationshipsSections
    #    - seeAlsoSections
    #    - primaryContentSections
    
    # 3. Convert identifiers to JSON URLs
    # 4. Recursively process each URL
    # 5. Track processed URLs to avoid loops
```

## Data Extraction Process

### 1. Title & Description
```python
title = metadata.get('title')
abstract = ' '.join(
    item['text'] for item in json_data.get('abstract', [])
    if item.get('type') == 'text'
)
```

### 2. Platform Availability
```python
platforms = []
for p in metadata.get('platforms', []):
    platforms.append({
        'platform': p['name'],
        'version': f"{p.get('introducedAt', '?')}+",
        'deprecated': p.get('deprecated', False)
    })
```

### 3. Code Declarations
```python
for section in primary_content:
    if section.get('kind') == 'declarations':
        tokens = declaration.get('tokens', [])
        code = ''.join(token.get('text', '') for token in tokens)
```

### 4. Content Paragraphs
```python
for item in content:
    if item.get('type') == 'paragraph':
        text_parts = []
        for inline in item.get('inlineContent', []):
            if inline.get('type') == 'text':
                text_parts.append(inline['text'])
            elif inline.get('type') == 'codeVoice':
                text_parts.append(f"`{inline['code']}`")
```

## Performance Optimizations

### 1. Concurrent Processing
```python
async def scrape_all(self, max_concurrent=10):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def scrape_with_limit(url):
        async with semaphore:
            return await self.scrape_url(url)
    
    tasks = [scrape_with_limit(url) for url in urls]
    await asyncio.gather(*tasks)
```

### 2. Adaptive Rate Limiting
```python
class AdaptiveRateLimiter:
    def __init__(self):
        self.delay = 0.1  # Start with 100ms
    
    async def wait(self):
        await asyncio.sleep(self.delay)
    
    def adjust(self, status_code):
        if status_code == 429:  # Too Many Requests
            self.delay *= 2  # Exponential backoff
        elif status_code == 200:
            self.delay *= 0.9  # Gradually speed up
```

### 3. Memory Efficiency
- Process in batches
- Use generators for large datasets
- Clear processed data from memory
- Write to disk incrementally

## Error Handling

```python
async def fetch_with_retry(self, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = await self.client.get(url)
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                await self.rate_limiter.wait()
            elif response.status_code == 404:
                return None  # Page doesn't exist
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)
```

## Storage Structure

```
documentation/
├── swiftui/
│   ├── text.md
│   ├── button.md
│   ├── view/
│   │   ├── frame.md
│   │   └── padding.md
│   └── ...
├── uikit/
├── foundation/
└── ...
```

## Markdown Output Format

```markdown
# [Title]

**Framework**: [Framework Name]

[Brief Description]

**Availability**:
- iOS 13.0+
- macOS 10.15+
- ...

## Declaration

```swift
[Code Declaration]
```

## Overview

[Detailed description paragraphs]

## Parameters

- `param1`: Description
- `param2`: Description

## Topics

### [Topic Group]
- [Related API](link)
- [Another API](link)

## See Also

- [Related Documentation](link)

---

*[View on Apple Developer](original-url)*
```

## Testing Strategy

1. **Unit Tests**
   - URL transformation
   - JSON parsing
   - Markdown generation

2. **Integration Tests**
   - Single page scraping
   - Framework discovery
   - Error handling

3. **Performance Tests**
   - Concurrent request handling
   - Memory usage
   - Rate limiting

## Deployment Considerations

1. **Docker Container**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "-m", "scraper"]
   ```

2. **Environment Variables**
   - `MAX_CONCURRENT_REQUESTS`
   - `RATE_LIMIT_DELAY`
   - `OUTPUT_DIRECTORY`

3. **Monitoring**
   - Progress tracking
   - Error rates
   - Performance metrics

## Future Enhancements

1. **Incremental Updates**
   - Track content hashes
   - Only update changed pages
   - Webhook notifications

2. **Search Index**
   - Build searchable index
   - Full-text search
   - API autocomplete

3. **API Server**
   - REST API for documentation
   - GraphQL endpoint
   - WebSocket for real-time updates