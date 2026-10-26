---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(values:_:)-7wais"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(values:_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`ModelContext`](../modelcontext.md) with additional context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<V, R>(values: V, _ action: @Sendable (ModelContext, V) async throws -> R) async rethrows -> sending R where V : Sendable, R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(values:_:)-7wais)*