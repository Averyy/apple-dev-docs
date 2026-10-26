---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/choleskyinv(_:upper:stream:)"
framework: "mlx-swift/MLX"
---

# choleskyInv(_:upper:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the inverse of a real symmetric positive semi-definite matrix using it’s Cholesky decomposition.

## Declaration

```swift
func choleskyInv(_ array: MLXArray, upper: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the Cholesky decomposition is computed for each matrix in the last two dimensions of `a`.

If the input matrix is not a triangular matrix behavior is undefined.

## Parameters

- `array`: Input array
- `upper`: If true return the upper triangular Cholesky factor, otherwise the lower triangular Cholesky factor.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/choleskyinv(_:upper:stream:))*