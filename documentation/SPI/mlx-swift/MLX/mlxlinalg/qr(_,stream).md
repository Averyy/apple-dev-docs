---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/qr(_:stream:)"
framework: "mlx-swift/MLX"
---

# qr(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

The QR factorization of the input matrix.

## Declaration

```swift
static func qr(_ array: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray)
```

#### Return Value

The `Q` and `R` matrices

#### Discussion

This function supports arrays with at least 2 dimensions. The matrices which are factorized are assumed to be in the last two dimensions of the input.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/qr(_:stream:))*