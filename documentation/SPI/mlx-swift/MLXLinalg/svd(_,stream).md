---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/svd(_:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# svd(_:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

The Singular Value Decomposition (SVD) of the input matrix.

> **Deprecated**: svd is now available in the main MLX module

## Declaration

```swift
func svd(_ array: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray, MLXArray)
```

## Return Value

The `U`, `S`, and `Vt` matrices, such that `A = matmul(U, matmul(diag(S), Vt))`

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the function iterates over all indices of the first `array.ndim - 2` dimensions and for each combination SVD is applied to the last two indices.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/svd(_:stream:))*