---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/layernorm(_:weight:bias:eps:stream:)"
framework: "mlx-swift/MLX"
---

# layerNorm(_:weight:bias:eps:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Layer normalization.

## Declaration

```swift
static func layerNorm(_ x: MLXArray, weight: MLXArray? = nil, bias: MLXArray? = nil, eps: Float, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The normalization is with respect to the last axis of the input `x`.

## Parameters

- `x`: Input array
- `weight`: A multiplicative weight to scale the result by. The `weight` should be one-dimensional with the same size as the last axis of `x`.  If not given no scaling will occur.
- `bias`: An additive offset to be added to the result. The `bias` should be one-dimensional with the same size as the last axis of `x`.  It not given no offset will occur.
- `eps`: A small additive constant for numerical stability
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/layernorm(_:weight:bias:eps:stream:))*