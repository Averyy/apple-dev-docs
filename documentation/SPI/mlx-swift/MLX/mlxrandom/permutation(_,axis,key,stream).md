---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/permutation(_:axis:key:stream:)"
framework: "mlx-swift/MLX"
---

# permutation(_:axis:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate a random permutation of the entries of an array.

## Declaration

```swift
static func permutation(_ array: MLXArray, axis: Int = 0, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Permuted array

## Parameters

- `array`: Array to permute
- `axis`: Axis along which to permute
- `key`: PRNG key
- `stream`: Stream


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/permutation(_:axis:key:stream:))*