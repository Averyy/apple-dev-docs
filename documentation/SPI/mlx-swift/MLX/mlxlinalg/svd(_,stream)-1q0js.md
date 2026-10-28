---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/svd(_:stream:)-1q0js"
framework: "mlx-swift/MLX"
---

# svd(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

The Singular Value Decomposition (SVD) of the input matrix.

## Declaration

```swift
static func svd(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The `S` matrix

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the function iterates over all indices of the first `array.ndim - 2` dimensions and for each combination SVD is applied to the last two indices.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/svd(_:stream:)-1q0js)*