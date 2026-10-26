---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/qr(_:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# qr(_:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

The QR factorization of the input matrix.

> **Deprecated**: qr is now available in the main MLX module

## Declaration

```swift
func qr(_ array: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray)
```

#### Return Value

The `Q` and `R` matrices

#### Discussion

This function supports arrays with at least 2 dimensions. The matrices which are factorized are assumed to be in the last two dimensions of the input.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/qr(_:stream:))*