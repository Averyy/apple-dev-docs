---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/init(modelid:scorekind:memoryreporter:scoreoperation:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(modelID:scoreKind:memoryReporter:scoreOperation:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Create a type-erased reranker around a scoring operation.

## Declaration

```swift
init(modelID: String, scoreKind: RerankScoreKind, memoryReporter: (any ModelMemoryReporting)? = nil, scoreOperation: @escaping ScoreOperation)
```

## Discussion

The operation must return one finite score per document in original input order. Pass the container that owns the model as `memoryReporter` to support [`memory()`](./memory%28%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/init(modelid:scorekind:memoryreporter:scoreoperation:))*