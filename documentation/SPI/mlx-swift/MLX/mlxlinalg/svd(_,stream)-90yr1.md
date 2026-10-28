---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/svd(_:stream:)-90yr1"
framework: "mlx-swift/MLX"
---

# svd(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

The Singular Value Decomposition (SVD) of the input matrix.

## Declaration

```swift
static func svd(_ array: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray, MLXArray)
```

## Return Value

The `U`, `S`, and `Vt` matrices, such that `A = matmul(U, matmul(diag(S), Vt))`

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the function iterates over all indices of the first `array.ndim - 2` dimensions and for each combination SVD is applied to the last two indices.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/svd(_:stream:)-90yr1)*