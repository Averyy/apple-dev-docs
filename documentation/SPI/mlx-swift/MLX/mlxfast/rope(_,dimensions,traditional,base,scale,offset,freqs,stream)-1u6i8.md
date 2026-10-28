---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-1u6i8"
framework: "mlx-swift/MLX"
---

# RoPE(_:dimensions:traditional:base:scale:offset:freqs:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Optimized implementation of `NN.RoPE` with array offset for batched inference.

## Declaration

```swift
static func RoPE(_ array: MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: MLXArray, freqs: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The input with rotary positional encoding applied.

## Discussion

This overload accepts an array offset, allowing different position offsets for each sequence in a batch. The offset can be a scalar array or a vector with length matching the batch size.

## Parameters

- `array`: Input array
- `dimensions`: The feature dimensions to be rotated. If the input feature is larger than dims then the rest is left unchanged.
- `traditional`: If `true` choose the traditional implementation which is slightly less efficient.
- `base`: The base used to compute angular frequency for each dimension in the positional encodings.
- `scale`: The scale used to scale the positions.
- `offset`: The position offset as an array. Can be a scalar or a vector of offsets for each batch element.
- `freqs`: Optional frequencies to use with RoPE.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/rope(_:dimensions:traditional:base:scale:offset:freqs:stream:)-1u6i8)*