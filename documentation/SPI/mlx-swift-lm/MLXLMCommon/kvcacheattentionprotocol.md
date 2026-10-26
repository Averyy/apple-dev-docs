---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheattentionprotocol"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheAttentionProtocol

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for caches that can update and compute attention from their own storage layout.

## Declaration

```swift
protocol KVCacheAttentionProtocol : KVCache
```

#### Overview

Used by compressed caches such as [`VarianceNormalizedKVCache`](./variancenormalizedkvcache.md) that keep completed tiles in a non-materialized representation and compute scores/values via cache-native kernels (e.g. `quantizedMM` in a rotated domain).

## Topics

### Instance Methods
- [func updateAndAttend(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode) -> MLXArray](./kvcacheattentionprotocol/updateandattend%28queries,keys,values,scale,mask%29.md)
  Update the cache with new K/V tensors and compute attention without first returning a fully materialized cache tensor pair.

## Relationships

### Inherits From
- [KVCache](./kvcache.md)
- MLX.Evaluatable
### Conforming Types
- [VarianceNormalizedKVCache](./variancenormalizedkvcache.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheattentionprotocol)*