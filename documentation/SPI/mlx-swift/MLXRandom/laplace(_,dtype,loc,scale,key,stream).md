---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/laplace(_:dtype:loc:scale:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# laplace(_:dtype:loc:scale:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Sample numbers from a Laplace distribution.

> **Deprecated**: laplace is now available in the main MLX module

## Declaration

```swift
func laplace(_ shape: [Int] = [], dtype: DType = .float32, loc: Float = 0, scale: Float = 1, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Parameters

- `shape`: Shape of the output
- `dtype`: Type of the output
- `loc`: Mean of the distribution
- `scale`: Scale “b” of the distribution
- `key`: PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/laplace(_:dtype:loc:scale:key:stream:))*