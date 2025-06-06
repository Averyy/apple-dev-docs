# Apple Documentation RAG Implementation Plan

## Executive Summary

This plan outlines how to build a RAG system for Apple developer documentation, leveraging lessons learned from CatoTax while adapting for technical documentation's unique requirements. The goal is to create an MCP server that provides instant, accurate access to Apple's 100k+ pages of documentation directly within developer tools.

## Key Differences from CatoTax

### Content Characteristics
- **Code-heavy**: Swift/Objective-C examples, API signatures
- **Visual elements**: Diagrams, screenshots, UI examples
- **Versioning**: Multiple iOS/macOS versions simultaneously
- **Cross-references**: Heavy linking between frameworks
- **Updates**: Frequent during WWDC season, stable otherwise

### User Patterns
- **Query types**: "How to implement X", "What's the difference between Y and Z"
- **Context needs**: Full code examples, not just snippets
- **Speed critical**: Developers won't wait >300ms
- **Integration**: Must work seamlessly in Cursor/Claude Desktop

## Architecture Overview

```
Apple Docs → Scraper → Markdown → Chunker → Embeddings → Vector DB
                                      ↓
                                 MCP Server → Claude Desktop/Cursor
```

## Phase 1: Scraping Strategy (Week 1-2)

### Target Sources
1. **developer.apple.com/documentation/**
   - Swift/SwiftUI/UIKit references
   - Human Interface Guidelines
   - Sample code projects
   
2. **developer.apple.com/tutorials/**
   - SwiftUI tutorials
   - App development paths

3. **developer.apple.com/design/**
   - Design resources
   - UI patterns

### Scraper Design
```python
class AppleDocsScraper:
    """
    Key considerations:
    - Respect robots.txt and rate limits
    - Handle authentication if needed
    - Preserve code formatting perfectly
    - Extract version information
    """
    
    def scrape_framework_docs(self, framework: str):
        # Special handling for:
        # - Code blocks (preserve indentation)
        # - Swift vs Objective-C tabs
        # - Availability annotations (@available)
        # - See Also sections
        pass
```

### File Organization
```
apple_docs/
├── frameworks/
│   ├── SwiftUI/
│   │   ├── Views/
│   │   ├── Modifiers/
│   │   └── Protocols/
│   ├── UIKit/
│   └── Foundation/
├── tutorials/
├── hig/ (Human Interface Guidelines)
└── metadata.json
```

## Phase 2: Chunking Strategy (Week 2-3)

### Technical Documentation Chunking

**Different from legal docs:**
- Preserve complete code examples
- Keep function signatures with their descriptions
- Maintain tutorial step sequences
- Bundle related methods/properties

```python
class TechnicalChunkingStrategy:
    """
    Child chunks: 400-500 tokens (larger for code)
    Parent chunks: 3000-4000 tokens (full examples)
    """
    
    def chunk_rules(self):
        return {
            "preserve_code_blocks": True,
            "keep_signatures_whole": True,
            "group_related_methods": True,
            "maintain_tutorial_flow": True
        }
```

### Metadata Schema
```json
{
    "framework": "SwiftUI",
    "type": "View",
    "name": "List",
    "ios_version": "13.0+",
    "macos_version": "10.15+",
    "declaration": "struct List<SelectionValue, Content>",
    "topics": ["Collections", "User Interface"],
    "related": ["ForEach", "Section", "NavigationView"]
}
```

## Phase 3: Embedding Strategy (Week 3)

### Model Selection
For technical documentation, we're using:
- **Current**: BGE-M3 via TEI server (local, free)
- **Alternative**: `voyage-3-lite` ($0.89 for 278K docs)
- **Why BGE-M3**: Top MTEB performer, 8K context, perfect for technical docs

### Context Enhancement
```python
TECHNICAL_CONTEXT_TEMPLATE = """
Generate a 50-100 token context for this technical documentation chunk:

1. Framework and class/function name
2. Primary purpose and use case
3. Key parameters or modifiers
4. Common usage patterns
5. Version availability

Chunk: {chunk_content}
Metadata: {metadata}

Return ONLY the contextual summary.
"""
```

### Indexing Optimizations
- Index by iOS/macOS version for filtering
- Separate collections for frameworks vs tutorials
- Tag deprecated content appropriately

## Phase 4: MCP Server Implementation (Week 4)

### Server Architecture
```typescript
// mcp-server/src/index.ts
interface AppleDocsServer {
  search(query: string, options?: SearchOptions): Promise<SearchResult[]>
  getDocument(id: string): Promise<Document>
  getCodeExample(id: string): Promise<CodeExample>
}

interface SearchOptions {
  framework?: string
  minIOSVersion?: string
  includeDeprecated?: boolean
  maxResults?: number
}
```

### Key Features
1. **Smart filtering**: By framework, version, type
2. **Code extraction**: Return runnable examples
3. **Context awareness**: Understand current file type
4. **Fast response**: <300ms for common queries

### Integration Points
```typescript
// Cursor/Claude Desktop integration
const tools = {
  "search_apple_docs": {
    description: "Search Apple developer documentation",
    parameters: {
      query: { type: "string", required: true },
      framework: { type: "string", required: false }
    }
  },
  "get_swift_example": {
    description: "Get Swift code example for a specific API",
    parameters: {
      api: { type: "string", required: true }
    }
  }
}
```

## Phase 5: Retrieval Optimization

### Query Understanding
```python
def process_developer_query(query: str):
    # Detect intent
    if "how to" in query.lower():
        return "tutorial"
    elif "difference between" in query.lower():
        return "comparison"
    elif any(api in query for api in KNOWN_APIS):
        return "api_reference"
    
    # Expand abbreviations
    # "VStack" → "VStack vertical stack SwiftUI"
    # "NS" → "Foundation NSObject"
```

### Hybrid Search Weights
For technical docs, adjust weights:
- **Vector search**: 60% (semantic understanding)
- **BM25**: 40% (exact API names critical)

### Reranking Strategy
```python
def rerank_technical_results(results, query):
    # Boost factors:
    # - Exact API match: 2.0x
    # - Recent iOS version: 1.5x
    # - Complete code example: 1.3x
    # - Tutorial content: 1.2x
```

## Implementation Timeline

### Week 1-2: Scraping
- [ ] Set up Apple docs scraper
- [ ] Handle authentication/rate limits
- [ ] Test with SwiftUI framework first
- [ ] Validate markdown quality

### Week 3: Processing
- [ ] Implement code-aware chunking
- [ ] Add technical context generation
- [ ] Generate embeddings with voyage-3
- [ ] Build Chroma collections

### Week 4: MCP Server
- [ ] Create TypeScript MCP server
- [ ] Implement search endpoints
- [ ] Add code extraction features
- [ ] Test in Claude Desktop

### Week 5: Optimization
- [ ] Performance tuning
- [ ] Query understanding improvements
- [ ] A/B test retrieval strategies
- [ ] Add caching layer

## Cost Estimates

### One-time Processing
- Scraping: $0 (respectful rate limiting)
- Embeddings: $0 (local BGE-M3 via TEI)
- Processing time: 3-4 hours for 278K docs
- **Total**: $0 (just electricity)

### Ongoing Costs
- Updates: $0 (local processing)
- Query embeddings: $0 (local TEI server)
- Hosting: $0 (runs on existing infrastructure)

## Critical Success Factors

### 1. Code Preservation
```markdown
# Bad chunking
SwiftUI List view is used for...
```swift
struct ContentView: View {

# Good chunking  
SwiftUI List view is used for displaying collections:
```swift
struct ContentView: View {
    var body: some View {
        List(items) { item in
            Text(item.name)
        }
    }
}
```

### 2. Version Awareness
Always include iOS/macOS version requirements in context and filtering.

### 3. Speed
- Local Chroma instance recommended
- Aggressive caching for common queries
- Pre-compute embeddings for all queries

### 4. Developer Experience
```typescript
// Natural integration
// User types: "how to make a list in swiftui"
// MCP returns: Complete, runnable example with explanation
```

## Quality Benchmarks

### Accuracy Targets
- API reference queries: >95% accuracy
- Tutorial searches: >90% accuracy
- Code examples: 100% syntactically correct

### Performance Targets
- Search latency: <300ms (p95)
- MCP response: <500ms total
- Cache hit rate: >70% for common queries

## Maintenance Plan

### Update Schedule
- **Daily**: Check for new/updated docs
- **Weekly**: Full framework scan
- **WWDC Season**: Multiple daily updates
- **Stable Period**: Weekly updates sufficient

### Monitoring
- Query patterns to improve retrieval
- Failed searches to add coverage
- Performance metrics
- User feedback from Cursor integration

## Risk Mitigation

### Technical Risks
1. **API changes**: Version everything
2. **Rate limiting**: Implement respectful scraping
3. **Large code blocks**: Adjust chunk sizes dynamically

### Quality Risks
1. **Outdated info**: Clear version labeling
2. **Incomplete examples**: Always preserve full context
3. **Wrong framework**: Strong metadata filtering

## Full Implementation Scope

### Complete Coverage from Day One
1. **All Apple Frameworks**: SwiftUI, UIKit, Foundation, Core Data, etc.
2. **All Documentation Types**: References, tutorials, HIG, sample code
3. **All Platforms**: iOS, macOS, watchOS, tvOS, visionOS
4. **Performance**: <500ms responses across all queries
5. **Quality**: 90%+ accuracy across all frameworks

### Comprehensive Features
1. **Universal search** across all documentation
2. **Code extraction** with full context
3. **Version filtering** for all platforms
4. **Tutorial navigation** with step tracking
5. **API migration** suggestions
6. **Visual asset** retrieval where applicable

## Conclusion

This plan provides a comprehensive approach for building a technical documentation RAG system. The focus on code preservation, version awareness, and speed will create a valuable tool for Apple developers. The architecture is designed to handle the full scope of Apple's documentation from the start, ensuring developers have access to all resources they need in one unified interface.