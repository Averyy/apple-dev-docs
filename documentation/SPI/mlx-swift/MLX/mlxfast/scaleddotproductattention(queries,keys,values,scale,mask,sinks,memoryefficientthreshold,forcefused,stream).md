---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/scaleddotproductattention(queries:keys:values:scale:mask:sinks:memoryefficientthreshold:forcefused:stream:)"
framework: "mlx-swift/MLX"
---

# scaledDotProductAttention(queries:keys:values:scale:mask:sinks:memoryEfficientThreshold:forceFused:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`

## Declaration

```swift
static func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXArray?, sinks: MLXArray? = nil, memoryEfficientThreshold: Int? = nil, forceFused: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
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

In the following the dimensions are given by:

- `B`: The batch size.
- `N_q`: The number of query heads.
- `N_kv`: The number of key and value heads.
- `T_q`: The number of queries per example.
- `T_kv`: The number of keys and values per example.
- `D`: The per-head dimension.

## Parameters

- `queries`: Queries with shape `[B, N_q, T_q, D]`
- `keys`: Keys with shape `[B, N_kv, T_kv, D]`
- `values`: Values with shape `[B, N_kv, T_kv, D]`
- `scale`: Scale for queries, typically `1 / sqrt(q.dim(-1))`
- `mask`: Mask array
- `sinks`: Optional array of attention sinks
- `memoryEfficientThreshold`: Unused
- `forceFused`: If `true` use a fused kernel regardless of the heuristic choice.  This can result in slower kernels in some case but can also reduce memory consumption
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/scaleddotproductattention(queries:keys:values:scale:mask:sinks:memoryefficientthreshold:forcefused:stream:))*