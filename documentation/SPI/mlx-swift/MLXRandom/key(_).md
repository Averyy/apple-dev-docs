---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/key(_:)"
framework: "mlx-swift/MLXRandom"
---

# key(_:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Get a PRNG key from a seed.

> **Deprecated**: key is now available in the main MLX module

## Declaration

```swift
func key(_ seed: UInt64) -> MLXArray
```

#### Discussion

Return a value that can be used as a PRNG key.  All [MLXRandom](./MLXRandom.md) functions take an optional key – this will let you control the random number generation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/key(_:))*