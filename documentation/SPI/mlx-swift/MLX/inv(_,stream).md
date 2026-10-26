---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/inv(_:stream:)"
framework: "mlx-swift/MLX"
---

# inv(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the inverse of a square matrix.

## Declaration

```swift
func inv(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

`ainv` such that `dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])`

#### Discussion

This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of `array`.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/inv(_:stream:))*