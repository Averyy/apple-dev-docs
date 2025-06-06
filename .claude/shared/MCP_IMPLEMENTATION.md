# MCP Server Implementation with TEI

## Architecture Overview

```
User Query → MCP Server → TEI Server → ChromaDB → Results
           (Public)     (Private)   (Private)
```

## Embedding Infrastructure

### TEI Server (BGE-M3)
- **Location**: Local network at 192.168.2.5
- **Model**: BAAI/bge-m3 (1024 dimensions)
- **Version**: TEI 1.2 (newer versions have issues)
- **Performance**: ~32 docs/second with batch size 4
- **Context**: 8192 tokens max
- **API Docs**: http://192.168.2.5/docs

### Cost Comparison
- **Previous (OpenAI)**: $5.86 for embeddings
- **Current (TEI)**: $0 (local processing)
- **Monthly queries**: $0 vs $0.06-150/month with APIs

## Processing Statistics
- **Documents**: 278,778 Apple documentation pages
- **Data size**: 1.17 GB markdown
- **Vector DB size**: ~1.1 GB (1024 dims × 278K docs)
- **Initial indexing**: 3-4 hours
- **Query response**: <1000ms

## Security Model
1. **TEI Server**: Completely private (local network only)
2. **MCP Server**: Only public endpoint (with API key auth)
3. **Data**: Never leaves local network
4. **Embeddings**: Generated locally, stored locally

## Implementation Notes
- No OpenAI API key needed
- All embeddings done via TEI POST requests
- ChromaDB stores vectors + metadata
- MCP server translates queries through TEI

This architecture provides enterprise-grade semantic search with complete data privacy and zero ongoing costs.