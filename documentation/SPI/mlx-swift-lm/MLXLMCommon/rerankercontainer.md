---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankerContainer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

A thread-safe, type-erased reranker returned by model factories.

## Declaration

```swift
final class RerankerContainer
```

## Topics

### Initializers
- [init(modelID: String, scoreKind: RerankScoreKind, scoreOperation: ScoreOperation)](./rerankercontainer/init%28modelid,scorekind,scoreoperation%29.md)
  Create a type-erased reranker around a scoring operation.
### Instance Properties
- [let modelID: String](./rerankercontainer/modelid.md)
  Identifier of the loaded model.
- [let scoreKind: RerankScoreKind](./rerankercontainer/scorekind.md)
  Semantic meaning and numeric range of returned scores.
### Instance Methods
- [func scores(query: String, documents: [String], instruction: String?, options: RerankExecutionOptions) async throws -> RerankResponse](./rerankercontainer/scores%28query,documents,instruction,options%29.md)
  Score documents while preserving their original order.
### Type Aliases
- [RerankerContainer.ScoreOperation](./rerankercontainer/scoreoperation.md)
  Architecture-specific scoring operation stored by the type-erased container.
### Default Implementations
- [Reranker Implementations](./rerankercontainer/reranker-implementations.md)

## Relationships

### Conforms To
- [Reranker](./reranker.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer)*