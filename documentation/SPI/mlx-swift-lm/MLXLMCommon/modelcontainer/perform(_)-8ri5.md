---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(_:)-8ri5"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the model and/or tokenizer. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

> **Deprecated**: prefer perform(_:) that uses a ModelContext

## Declaration

```swift
func perform<R>(_ action: @Sendable (any LanguageModel, Tokenizer) throws -> sending R) async rethrows -> sending R where R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(_:)-8ri5)*