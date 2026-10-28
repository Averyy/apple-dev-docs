---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/rmsnorm(_:weight:eps:stream:)"
framework: "mlx-swift/MLXFast"
---

# rmsNorm(_:weight:eps:stream:)

**Framework**: mlx-swift/MLXFast  
**Kind**: func  
**Role**: Function

Root Mean Square normalization (RMS norm).

> **Deprecated**: rmsNorm is now available in the main MLX module

## Declaration

```swift
func rmsNorm(_ x: MLXArray, weight: MLXArray, eps: Float, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The normalization is with respect to the last axis of the input `x`.

## Parameters

- `x`: Input array
- `weight`: A multiplicative weight to scale the result by. The `weight` should be one-dimensional with the same size as the last axis of `x`.
- `eps`: A small additive constant for numerical stability
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/rmsnorm(_:weight:eps:stream:))*