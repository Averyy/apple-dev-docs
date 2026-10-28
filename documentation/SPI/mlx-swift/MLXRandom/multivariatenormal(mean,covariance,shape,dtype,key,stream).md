---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/multivariatenormal(mean:covariance:shape:dtype:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# multivariateNormal(mean:covariance:shape:dtype:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate jointly-normal random samples given a mean and covariance.

> **Deprecated**: multivariateNormal is now available in the main MLX module

## Declaration

```swift
func multivariateNormal(mean: MLXArray, covariance: MLXArray, shape: [Int] = [], dtype: DType = .float32, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The matrix `covariance` must be positive semi-definite. The behavior is undefined if it is not.  The only supported `dtype` is `.float32`.

## Parameters

- `mean`: Array of shape `[..., n]`, the mean of the distribution.
- `covariance`: Array  of shape `[..., n, n]`, the covariance matrix of the distribution. The batch shape `...` must be broadcast-compatible with that of `mean`.
- `shape`: The output shape must be broadcast-compatible with `mean.shape.dropLast()` and `covariance.shape.dropLast(2)`. If empty, the result shape is determined by broadcasting the batch shapes of `mean` and `covariance`.
- `dtype`: DType of the result
- `key`: PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/multivariatenormal(mean:covariance:shape:dtype:key:stream:))*