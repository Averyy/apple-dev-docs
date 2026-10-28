---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/det(_:stream:)"
framework: "mlx-swift/MLX"
---

# det(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Compute the determinant of a square matrix.

## Declaration

```swift
static func det(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the determinant is computed for each matrix in the last two dimensions.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/det(_:stream:))*