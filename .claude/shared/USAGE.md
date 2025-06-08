# Usage Guide

## Quick Commands

### Production Scraping (All Frameworks)
```bash
# Scrape all 341 frameworks with confirmation
python3 scrape.py --all --yes

# With ETags collected, incremental updates are extremely fast
# Initial run: ~3-4 hours for 278,778 pages
# Update runs: ~30 minutes (mostly 304 Not Modified responses)
```

### Specific Framework Scraping
```bash
# Scrape individual frameworks
python3 scrape.py --frameworks SwiftUI UIKit Foundation --yes

# Available frameworks include:
# SwiftUI, UIKit, Foundation, Metal, AVFoundation, Core Data, etc.
```

### Resume Interrupted Scraping
```bash
# Resume from where you left off
python3 scrape.py --resume --yes
```

### Incremental Updates (Recommended)
```bash
# Check for updates using ETag optimization
python3 scrape.py --all --yes

# ETag system automatically detects changes
# Only modified pages are re-scraped
# Typical update: <1% of pages changed
```

## Output Structure

All documentation is saved to `documentation/` directory:

```
documentation/
├── Accelerate/          # 2,042 pages
├── Accessibility/       # 258 pages  
├── AdServices/          # 15 pages
├── Foundation/          # 25,000+ pages
├── SwiftUI/            # 2,800+ pages
├── UIKit/              # 15,000+ pages
└── ...                 # 341 total frameworks, 278,778 total pages
```

## Features

- **Cross-framework links**: "Conforms To" sections link to local .md files
- **Code examples**: Preserved with syntax highlighting
- **Platform availability**: iOS, macOS, watchOS, tvOS version info
- **Incremental updates**: ETag-based change detection, extremely efficient
- **Rate limiting**: Respects Apple's servers (0.2s delays, 10 concurrent)

## MCP Server Integration

After scraping, the documentation is indexed locally for semantic search:

```
Query: "SwiftUI list"
Result: Documentation for SwiftUI List component with examples

Query: "Metal shader"  
Result: Metal shading language documentation and examples
```

All queries are processed through the local MCP server with zero API costs.

## Troubleshooting

### Scraping Errors
- **Rate limiting**: Automatic retry with exponential backoff
- **Network errors**: Will retry failed requests
- **Incomplete scraping**: Use `--resume` to continue

### Large Memory Usage
- Framework scraping is batched to manage memory
- Hash caching prevents duplicate processing
- Consider scraping frameworks individually for very limited memory

### Missing Content
- Some older APIs may not have JSON endpoints
- These will be logged and skipped automatically