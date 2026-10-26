---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(nonsendable:_:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# perform(nonSendable:_:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`EmbedderModelContext`](../embeddermodelcontext.md) with additional (non `Sendable`) context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<V, R>(nonSendable values: consuming V, _ action: @Sendable (EmbedderModelContext, V) async throws -> R) async rethrows -> sending R where R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(nonsendable:_:))*