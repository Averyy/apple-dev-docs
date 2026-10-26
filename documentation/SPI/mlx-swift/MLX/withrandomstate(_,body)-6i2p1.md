---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/withrandomstate(_:body:)-6i2p1"
framework: "mlx-swift/MLX"
---

# withRandomState(_:body:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Use the given [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) scoped to the current task and body.

## Declaration

```swift
func withRandomState<R>(_ state: MLXRandom.RandomState, body: () throws -> R) rethrows -> R
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/withrandomstate(_:body:)-6i2p1)*