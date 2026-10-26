---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/scoreoperation"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankerContainer.ScoreOperation

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: typealias  
**Role**: Type Alias

Architecture-specific scoring operation stored by the type-erased container.

## Declaration

```swift
typealias ScoreOperation = @Sendable (_ query: String, _ documents: [String], _ instruction: String?, _ options: RerankExecutionOptions) async throws -> [Double]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/scoreoperation)*