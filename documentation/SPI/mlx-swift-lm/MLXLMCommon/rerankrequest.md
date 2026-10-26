---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankrequest"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankRequest

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A request to score and order candidate documents by relevance to a query.

## Declaration

```swift
struct RerankRequest
```

## Topics

### Initializers
- [init(query: String, documents: [String], instruction: String?, topK: Int?, minimumScore: Double?)](./rerankrequest/init%28query,documents,instruction,topk,minimumscore%29.md)
  Create a request for sorted reranking.
### Instance Properties
- [var documents: [String]](./rerankrequest/documents.md)
  Candidate documents to score.
- [var instruction: String?](./rerankrequest/instruction.md)
  Optional model instruction for instruction-aware rerankers.
- [var minimumScore: Double?](./rerankrequest/minimumscore.md)
  Optional inclusive lower score bound.
- [var query: String](./rerankrequest/query.md)
  The search query or user intent.
- [var topK: Int?](./rerankrequest/topk.md)
  Maximum number of highest-scoring results to return.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankrequest)*