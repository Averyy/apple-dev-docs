---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontainer/perform(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Perform an action on the [`MTPDrafterContext`](../mtpdraftercontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Declaration

```swift
func perform<R>(_ action: @Sendable (MTPDrafterContext) async throws -> sending R) async rethrows -> sending R where R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontainer/perform(_:))*