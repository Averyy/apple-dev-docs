---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/solvetriangular(_:_:upper:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# solveTriangular(_:_:upper:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

Computes the solution of a triangular system of linear equations `AX = B`.

> **Deprecated**: solveTriangular is now available in the main MLX module

## Declaration

```swift
func solveTriangular(_ a: MLXArray, _ b: MLXArray, upper: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

-Parameters:

- a: input array.
- b: input array.
- upper: Whether the array is upper or lower triangular
- stream: stream or device


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/solvetriangular(_:_:upper:stream:))*