---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/pinv(_:stream:)"
framework: "mlx-swift/MLX"
---

# pinv(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the (Moore-Penrose) pseudo-inverse of a matrix.

## Declaration

```swift
func pinv(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

`aplus` such that `a @ aplus @ a = a`

## Discussion

This function calculates a generalized inverse of a matrix using its singular-value decomposition. This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of `array`.

## Parameters

- `array`: Input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/pinv(_:stream:))*