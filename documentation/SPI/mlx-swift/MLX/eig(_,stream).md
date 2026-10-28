---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eig(_:stream:)"
framework: "mlx-swift/MLX"
---

# eig(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the eigenvalues and eigenvectors of a square matrix.

## Declaration

```swift
func eig(_ array: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray)
```

## Return Value

A tuple containing the eigenvalues and the normalized right eigenvectors. The column `v[0..., i]` is the eigenvector corresponding to the i-th eigenvalue.

## Discussion

This function differs from `numpy.linalg.eig` in that the return type is always complex even if the eigenvalues are all real.

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues and eigenvectors are computed for each matrix in the last two dimensions.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eig(_:stream:))*