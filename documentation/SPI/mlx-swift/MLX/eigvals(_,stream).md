---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eigvals(_:stream:)"
framework: "mlx-swift/MLX"
---

# eigvals(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the eigenvalues of a square matrix.

## Declaration

```swift
func eigvals(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

The eigenvalues (not necessarily in order)

#### Discussion

This function differs from `numpy.linalg.eigvals` in that the return type is always complex even if the eigenvalues are all real.

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues are computed for each matrix in the last two dimensions.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/eigvals(_:stream:))*