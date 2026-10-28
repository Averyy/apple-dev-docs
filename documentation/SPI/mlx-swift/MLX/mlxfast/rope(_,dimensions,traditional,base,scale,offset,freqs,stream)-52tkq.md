---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-52tkq"
framework: "mlx-swift/MLX"
---

# RoPE(_:dimensions:traditional:base:scale:offset:freqs:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Optimized implementation of `NN.RoPE`.

## Declaration

```swift
static func RoPE(_ array: MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: Int, freqs: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-52tkq)*