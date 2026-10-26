---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankresponse"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankResponse

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The result of a reranking operation.

## Declaration

```swift
struct RerankResponse
```

## Topics

### Initializers
- [init(modelID: String, scoreKind: RerankScoreKind, results: [RerankResult])](./rerankresponse/init%28modelid,scorekind,results%29.md)
### Instance Properties
- [let modelID: String](./rerankresponse/modelid.md)
  Identifier of the model that produced the scores.
- [let results: [RerankResult]](./rerankresponse/results.md)
  Scored documents in original or descending relevance order, depending on the API used.
- [let scoreKind: RerankScoreKind](./rerankresponse/scorekind.md)
  Semantic meaning and numeric range of [`results`](./rerankresponse/results.md) scores.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankresponse)*