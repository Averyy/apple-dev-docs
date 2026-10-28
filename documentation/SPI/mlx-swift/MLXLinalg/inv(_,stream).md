---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/inv(_:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# inv(_:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

Compute the inverse of a square matrix.

> **Deprecated**: inv is now available in the main MLX module

## Declaration

```swift
func inv(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

`ainv` such that `dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])`

## Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of `array`.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/inv(_:stream:))*