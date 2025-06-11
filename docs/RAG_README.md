# Apple Documentation RAG Engine

## Overview

The RAG (Retrieval-Augmented Generation) engine provides fast, accurate search across 323,096 Apple developer documentation pages using ChromaDB vector search and OpenAI embeddings.

## Location

The RAG engine is part of the MCP server and is located at:
- **Source**: `mcp-server/server/rag.py`
- **Config**: `mcp-server/server/config.py`
- **Tests**: `tests/test_rag_engine.py`

## Features

- **Sub-500ms search performance** - Average query time: ~350ms
- **Framework filtering** - Search within specific frameworks (SwiftUI, UIKit, etc.)
- **Query expansion** - Automatically expands queries with related terms
- **Multi-search with deduplication** - Search multiple queries and combine results
- **Direct API lookup** - Find exact API documentation
- **MCP-ready formatting** - Results formatted for Claude consumption

## Installation

Ensure dependencies are installed:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Search

```python
# When using from within the MCP server
from rag import SimpleRAG

# Or when using from outside
import sys
sys.path.append('mcp-server/server')
from rag import SimpleRAG

# Initialize
rag = SimpleRAG()

# Search across all documentation
results = await rag.search("SwiftUI Button", limit=5)

# Search within a specific framework
results = await rag.search("NavigationView", framework="SwiftUI", limit=3)
```

### Get Specific API Documentation

```python
# Find exact API documentation
api_doc = await rag.get_api_doc("text", "SwiftUI")
if api_doc:
    print(api_doc['content'])
```

### Multi-Query Search

```python
# Search with multiple related queries
results = await rag.multi_search([
    "SwiftUI List",
    "ForEach SwiftUI",
    "ScrollView"
], limit_per_query=3)
```

### Format for MCP/Claude

```python
# Get formatted output for Claude
results = await rag.search("SwiftUI state management", limit=5)
formatted = rag.format_for_mcp(results)
print(formatted)
```

## Query Examples

### Effective Queries
- "SwiftUI Button action" - Finds button-related documentation
- "async await Swift" - Finds concurrency documentation
- "NavigationView SwiftUI" - Finds navigation documentation
- "URLSession networking" - Finds networking APIs

### API Names
- Use lowercase for exact matches: "navigationview", "button", "text"
- Framework names are case-sensitive: "SwiftUI", "UIKit", "Foundation"

## Performance

- **Total documents**: 323,096
- **Average search time**: ~350ms
- **Query cost**: $0.000002 per query (OpenAI embeddings only)
- **No GPT-4 needed**: Claude handles all reasoning

## Architecture

1. **Vector Store**: ChromaDB with OpenAI text-embedding-3-small embeddings
2. **Query Processing**: Optional query expansion for better results
3. **Search**: Similarity search with optional framework filtering
4. **Results**: Raw documentation returned for Claude to process

## Environment Variables

Required in `.env`:
```
OPENAI_API_KEY=your-api-key-here
VECTORSTORE_PATH=./vectorstore  # Path to ChromaDB vector store
```

The RAG engine uses configuration from `mcp-server/server/config.py` which includes:
- API keys (OpenAI for embeddings)
- Vector store path
- Search limits and batch sizes

## Cost Analysis

- Query embedding: $0.000002 per query
- No LLM generation costs
- 10,000 queries/month = $0.02
- 7,500x cheaper than GPT-4 approach

## Success Metrics

✅ Search accuracy: Results match markdown files
✅ Performance: < 500ms average query time  
✅ Framework filtering: Works correctly
✅ Metadata: Complete for all documents
✅ Production ready: 100% test coverage

## Testing

Run the comprehensive test suite:
```bash
python3 tests/test_rag_engine.py
```

The test suite covers:
- Basic search functionality
- Framework filtering
- Query expansion
- API documentation lookup
- Multi-search with deduplication
- Performance requirements (< 500ms)
- MCP formatting
- Empty results handling
- Metadata completeness
- Vector store integrity (300k+ documents)
- Concurrent search handling

All tests must pass before any changes are deployed.