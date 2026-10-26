---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(values:_:)-9yn9t"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(values:_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the model and/or tokenizer with additional context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

> **Deprecated**: prefer perform(values:_:) that uses a ModelContext

## Declaration

```swift
func perform<V, R>(values: V, _ action: @Sendable (any LanguageModel, Tokenizer, V) throws -> sending R) async rethrows -> sending R where V : Sendable, R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(values:_:)-9yn9t)*