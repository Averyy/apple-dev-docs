---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/permutation(_:key:stream:)"
framework: "mlx-swift/MLX"
---

# permutation(_:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate a random permutation of integers from `0` to `max`.

## Declaration

```swift
static func permutation(_ max: Int, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Permuted array

## Parameters

- `max`: Max value to permute
- `key`: PRNG key
- `stream`: Stream


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/permutation(_:key:stream:))*