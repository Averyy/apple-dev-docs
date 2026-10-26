---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankdocumentsresponse"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankDocumentsResponse

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The result of scoring or reranking structured documents.

## Declaration

```swift
struct RerankDocumentsResponse
```

## Topics

### Initializers
- [init(modelID: String, scoreKind: RerankScoreKind, results: [RerankedDocument])](./rerankdocumentsresponse/init%28modelid,scorekind,results%29.md)
### Instance Properties
- [let modelID: String](./rerankdocumentsresponse/modelid.md)
  Identifier of the model that produced the scores.
- [let results: [RerankedDocument]](./rerankdocumentsresponse/results.md)
  Structured document results in original or descending relevance order.
- [let scoreKind: RerankScoreKind](./rerankdocumentsresponse/scorekind.md)
  Semantic meaning and numeric range of [`results`](./rerankdocumentsresponse/results.md) scores.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankdocumentsresponse)*