---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/resolve(key:)"
framework: "mlx-swift/MLX"
---

# resolve(key:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Resolve the given key to a concrete MLXArray (random key).

## Declaration

```swift
func resolve(key: (some RandomStateOrKey)? = MLXArray?.none) -> MLXArray
```

#### Discussion

This will use the following values (in order until one is found) to resolve the random key:

- the passed key, either an [`MLXArray`](./mlxarray.md) or [`MLXRandom.RandomState`](./mlxrandom/randomstate.md)
- the task-local [`MLXRandom.RandomState`](./mlxrandom/randomstate.md), see [`withRandomState(_:body:)`](./withrandomstate%28_,body%29-18ob4.md)
- the global RandomState, [`globalState`](./mlxrandom/globalstate.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/resolve(key:))*