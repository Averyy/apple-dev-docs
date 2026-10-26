---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/init(modelid:scorekind:scoreoperation:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(modelID:scoreKind:scoreOperation:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Create a type-erased reranker around a scoring operation.

## Declaration

```swift
init(modelID: String, scoreKind: RerankScoreKind, scoreOperation: @escaping ScoreOperation)
```

#### Discussion

The operation must return one finite score per document in original input order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/init(modelid:scorekind:scoreoperation:))*