---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/eigvalsh(_:uplo:stream:)"
framework: "mlx-swift/MLX"
---

# eigvalsh(_:UPLO:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

## Declaration

```swift
static func eigvalsh(_ array: MLXArray, UPLO: String = "L", stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

The eigenvalues in ascending order

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues are computed for each matrix in the last two dimensions.

> **Note**: The input matrix is assumed to be symmetric (or Hermitian). Only the selected triangle is used. No checks for symmetry are performed.

## Parameters

- `array`: Input array. Must be a real symmetric or complex Hermitian matrix.
- `UPLO`: Whether to use the upper (`"U"`) or lower (`"L"`) triangle of the matrix. Default is `"L"`.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/eigvalsh(_:uplo:stream:))*