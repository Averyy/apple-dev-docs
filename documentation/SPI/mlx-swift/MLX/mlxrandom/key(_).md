---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/key(_:)"
framework: "mlx-swift/MLX"
---

# key(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Get a PRNG key from a seed.

## Declaration

```swift
static func key(_ seed: UInt64) -> MLXArray
```

#### Discussion

Return a value that can be used as a PRNG key.  All [`MLXRandom`](../mlxrandom.md) functions take an optional key – this will let you control the random number generation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/key(_:))*