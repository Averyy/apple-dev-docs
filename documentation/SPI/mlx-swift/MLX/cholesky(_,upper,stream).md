---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cholesky(_:upper:stream:)"
framework: "mlx-swift/MLX"
---

# cholesky(_:upper:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.

## Declaration

```swift
func cholesky(_ array: MLXArray, upper: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the Cholesky decomposition is computed for each matrix in the last two dimensions of `a`.

If the input matrix is not symmetric positive semi-definite, behavior is undefined.

## Parameters

- `array`: Input array
- `upper`: If true return the upper triangular Cholesky factor, otherwise the lower triangular Cholesky factor.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cholesky(_:upper:stream:))*