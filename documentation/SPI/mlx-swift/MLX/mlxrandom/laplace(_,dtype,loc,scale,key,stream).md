---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/laplace(_:dtype:loc:scale:key:stream:)"
framework: "mlx-swift/MLX"
---

# laplace(_:dtype:loc:scale:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Sample numbers from a Laplace distribution.

## Declaration

```swift
static func laplace(_ shape: some Collection<Int> = [], dtype: DType, loc: Float = 0, scale: Float = 1, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Parameters

- `shape`: Shape of the output
- `dtype`: Type of the output
- `loc`: Mean of the distribution
- `scale`: Scale “b” of the distribution
- `key`: Optional PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/laplace(_:dtype:loc:scale:key:stream:))*