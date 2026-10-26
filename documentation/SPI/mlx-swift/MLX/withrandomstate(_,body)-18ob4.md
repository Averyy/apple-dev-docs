---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/withrandomstate(_:body:)-18ob4"
framework: "mlx-swift/MLX"
---

# withRandomState(_:body:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Use the given [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) scoped to the current task and body.

## Declaration

```swift
func withRandomState<R>(_ state: MLXRandom.RandomState, body: () async throws -> R) async rethrows -> R
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/withrandomstate(_:body:)-18ob4)*