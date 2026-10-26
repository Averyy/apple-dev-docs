---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(nonsendable:_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(nonSendable:_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`ModelContext`](../modelcontext.md) with additional (non `Sendable`) context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<V, R>(nonSendable values: consuming V, _ action: @Sendable (ModelContext, V) async throws -> R) async rethrows -> sending R where R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(nonsendable:_:))*