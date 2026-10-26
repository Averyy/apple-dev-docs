---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-94hyd"
framework: "mlx-swift/MLX"
---

# RoPE(_:dimensions:traditional:base:scale:offset:freqs:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Optimized implementation of `NN.RoPE` with array offset for batched inference.

## Declaration

```swift
func RoPE(_ array: MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: MLXArray, freqs: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

> **Note**: `MLXNN.RoPE` uses this implementation internally.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-94hyd)*