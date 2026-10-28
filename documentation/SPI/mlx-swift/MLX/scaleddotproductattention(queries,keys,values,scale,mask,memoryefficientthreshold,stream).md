---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/scaleddotproductattention(queries:keys:values:scale:mask:memoryefficientthreshold:stream:)"
framework: "mlx-swift/MLX"
---

# scaledDotProductAttention(queries:keys:values:scale:mask:memoryEfficientThreshold:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`

## Declaration

```swift
func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXArray?, memoryEfficientThreshold: Int? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Supports [Multi-Head Attention](https://arxiv.org/abs/1706.03762), [Grouped Query Attention](https://arxiv.org/abs/2305.13245), and [Multi-Query Attention](https://arxiv.org/abs/1911.02150).

This function will dispatch to an optimized Metal kernel when the query sequence length is 1. It handles other cases with regular MLX operations.

> **Note**: The softmax operation is performed in float32 precision regardless of input precision (float16 or float32).

> **Note**: For Grouped Query Attention and Multi-Query Attention, the input arrays for `key` and `value` should not be pre-tiled to match the `query` array.

Specifically this implements:

```swift
var scores = (queries * self.scale).matmul(keys.transposed(0, 1, 3, 2))
if let mask {
    scores = scores + mask
}

scores = softMax(scores.asType(.float32), axis: -1).asType(scores.dtype)

return matmul(scores, values).transposed(0, 2, 1, 3)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/scaleddotproductattention(queries:keys:values:scale:mask:memoryefficientthreshold:stream:))*