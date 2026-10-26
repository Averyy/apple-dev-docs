---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/slogdet(_:stream:)"
framework: "mlx-swift/MLX"
---

# slogdet(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the sign and natural log of the absolute value of the determinant of a square matrix.

## Declaration

```swift
func slogdet(_ array: MLXArray, stream: StreamOrDevice = .default) -> (sign: MLXArray, logabsdet: MLXArray)
```

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the sign and log-absolute-determinant are computed for each matrix in the last two dimensions.

For a singular matrix, `sign` is 0 and `logabsdet` is `-inf`.

The determinant can be reconstructed as `det = sign * exp(logabsdet)`. This is more numerically stable than computing the determinant directly for matrices with large or small determinants.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/slogdet(_:stream:))*