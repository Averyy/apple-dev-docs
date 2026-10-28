---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eigh(_:uplo:stream:)"
framework: "mlx-swift/MLX"
---

# eigh(_:UPLO:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.

## Declaration

```swift
func eigh(_ array: MLXArray, UPLO: String = "L", stream: StreamOrDevice = .default) -> (MLXArray, MLXArray)
```

## Return Value

A tuple containing the eigenvalues in ascending order and the normalized eigenvectors. The column `v[0..., i]` is the eigenvector corresponding to the i-th eigenvalue.

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues and eigenvectors are computed for each matrix in the last two dimensions.

> **Note**: The input matrix is assumed to be symmetric (or Hermitian). Only the selected triangle is used. No checks for symmetry are performed.

## Parameters

- `array`: Input array. Must be a real symmetric or complex Hermitian matrix.
- `UPLO`: Whether to use the upper (`"U"`) or lower (`"L"`) triangle of the matrix. Default is `"L"`.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eigh(_:uplo:stream:))*