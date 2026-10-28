---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(_:)-629d0"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`ModelContext`](../modelcontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<R>(_ action: @Sendable (ModelContext) async throws -> sending R) async rethrows -> sending R where R : Sendable
```

## Discussion

> **Note**: The closure receives `ModelContext` which is not `Sendable`. This is intentional - the closure runs within the actor’s isolation, ensuring thread-safe access to the model.

> **Note**: The `sending` keyword indicates the return value is transferred (not shared) across isolation boundaries, allowing non-Sendable types to be safely returned.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/perform(_:)-629d0)*