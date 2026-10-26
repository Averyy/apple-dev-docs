---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/lu(_:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# lu(_:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

Compute the LU factorization of the given matrix `A`.

> **Deprecated**: lu is now available in the main MLX module

## Declaration

```swift
func lu(_ a: MLXArray, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray, MLXArray)
```

#### Discussion

Note, unlike the default behavior of `scipy.linalg.lu`, the pivots are indices. To reconstruct the input use `L[P] @ U` for 2 dimensions or `takeAlong(L, P[.ellipsis, .newAxis], axis: -2) @ U` for more than 2 dimensions.

To construct the full permuation matrix do:

P = putAlong(zeros(L), p[.ellipsis, .newAxis], MLXArray(1.0), axis: -1)

-Parameters:

- a: input array.
- stream: stream or device


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/lu(_:stream:))*