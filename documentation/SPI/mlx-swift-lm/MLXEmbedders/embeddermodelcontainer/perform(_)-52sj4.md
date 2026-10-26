---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(_:)-52sj4"
framework: "mlx-swift-lm/MLXEmbedders"
---

# perform(_:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`EmbedderModelContext`](../embeddermodelcontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<R>(_ action: @Sendable (EmbedderModelContext) async throws -> sending R) async rethrows -> sending R where R : Sendable
```

#### Discussion

> **Note**: The closure receives `EmbedderModelContext` which is not `Sendable`. This is intentional - the closure runs within the actor’s isolation, ensuring thread-safe access to the model.

> **Note**: The `sending` keyword indicates the return value is transferred (not shared) across isolation boundaries, allowing non-Sendable types to be safely returned.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(_:)-52sj4)*