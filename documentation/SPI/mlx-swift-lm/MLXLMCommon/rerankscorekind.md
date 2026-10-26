---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankscorekind"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankScoreKind

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

The semantic meaning and numeric range of scores returned by a reranker.

## Declaration

```swift
enum RerankScoreKind
```

## Topics

### Enumeration Cases
- [RerankScoreKind.cosineSimilarity](./rerankscorekind/cosinesimilarity.md)
  Cosine similarity in the closed range `-1...1`.
- [RerankScoreKind.logit](./rerankscorekind/logit.md)
  An unbounded model logit.
- [RerankScoreKind.normalizedRelevance](./rerankscorekind/normalizedrelevance.md)
  A model-specific relevance score normalized to the closed range `0...1`.
### Default Implementations
- [Equatable Implementations](./rerankscorekind/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankscorekind)*