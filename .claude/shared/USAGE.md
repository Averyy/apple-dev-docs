# Usage Guide

## Quick Commands

### Production Scraping (All Frameworks)
```bash
# Scrape all 342+ frameworks with confirmation
python3 scrape.py --all --yes

# This will take approximately 3-4 hours for complete scraping
# Results: ~100,000+ markdown files in documentation/ directory
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

### Re-scraping with Updates
```bash
# Clear hash cache to force re-scraping (applies latest fixes)
python3 scripts/utilities/rescrape_existing.py --clear-hashes

# Then run the scraper again
python3 scrape.py --all --yes
```

## Output Structure

All documentation is saved to `documentation/` directory:

```
documentation/
├── Accelerate/          # 4,420+ pages
├── Accessibility/       # 115+ pages  
├── AdServices/          # 10+ pages
├── Foundation/          # 2,000+ pages
├── SwiftUI/            # 1,500+ pages
├── UIKit/              # 3,000+ pages
└── ...                 # 342+ total frameworks
```

## Features

- **Cross-framework links**: "Conforms To" sections link to local .md files
- **Code examples**: Preserved with syntax highlighting
- **Platform availability**: iOS, macOS, watchOS, tvOS version info
- **Incremental updates**: Only re-scrapes changed content
- **Rate limiting**: Respects Apple's servers (0.2s delays)

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