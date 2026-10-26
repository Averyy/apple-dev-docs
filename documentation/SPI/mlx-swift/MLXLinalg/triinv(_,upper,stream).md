---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/triinv(_:upper:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# triInv(_:upper:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

Compute the inverse of a triangular square matrix.

> **Deprecated**: triInv is now available in the main MLX module

## Declaration

```swift
func triInv(_ array: MLXArray, upper: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

`ainv` such that `dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])`

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of `array`.

## Parameters

- `array`: Input array
- `upper`: True if the array is an upper triangular matrix
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/triinv(_:upper:stream:))*