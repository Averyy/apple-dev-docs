---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)"
framework: "mlx-swift/MLXFast"
---

# RoPE(_:dimensions:traditional:base:scale:offset:freqs:stream:)

**Framework**: mlx-swift/MLXFast  
**Kind**: func  
**Role**: Function

Optimized implementation of `NN.RoPE`.

> **Deprecated**: RoPE is now available in the main MLX module

## Declaration

```swift
func RoPE(_ array: MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: Int, freqs: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Used like this:

```swift
let x: MLXArray
let dimensions: Int
let traditional: Bool
let base: Float
let scale: Float
let offset: Int

let shape = x.shape
var x = x.reshaped(-1, x.dim(-2), x.dim(-1))
x = MLXFast.RoPE(x, dimensions: dimensions, traditional: traditional, base: base, scale: scale, offset: offset)
return x.reshaped(shape)
```

> **Note**: `MLXNN.RoPE` uses this implementation internally.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:))*