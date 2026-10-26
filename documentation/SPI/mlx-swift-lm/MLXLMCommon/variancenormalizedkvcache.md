---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/variancenormalizedkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# VarianceNormalizedKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Variance-normalized KV cache following KVarN’s core tile-compression steps.

## Declaration

```swift
class VarianceNormalizedKVCache
```

#### Overview

This is intentionally implemented as a regular [`KVCache`](./kvcache.md) so model attention code can use it without changes. When called through [`attentionWithCacheUpdate(queries:keys:values:cache:scale:mask:)`](./attentionwithcacheupdate%28queries,keys,values,cache,scale,mask%29.md), completed tiles stay quantized on the hot path: attention scores and value products are computed with `quantizedMM` in the rotated domain, and only the final output is inverse-rotated. The tile normalization uses clipped log-domain dual-axis scale balancing with best-imbalance tracking, matching the central KVarN VarN algorithm more closely while remaining an MLX Swift implementation. The RTN affine scale/bias are fused into the matching variance-normalization axis so each completed tile stores compact K/V records: packed weights, fused affine scale, fused affine bias, and the remaining variance scale.

> ⚠️ **Warning**: This cache remains experimental pending model-level long-context quality gates and a fused MLX/Metal attention implementation. Use `attentionWithCacheUpdate` for decode; `update(keys:values:)` is a compatibility slow path.

## Topics

### Initializers
- [init(tileSize: Int, keyBits: Int, valueBits: Int, sinkhornIterations: Int)](./variancenormalizedkvcache/init%28tilesize,keybits,valuebits,sinkhorniterations%29.md)
### Instance Properties
- [var debugDescription: String](./variancenormalizedkvcache/debugdescription.md)
- [var isTrimmable: Bool](./variancenormalizedkvcache/istrimmable.md)
- [let keyBits: Int](./variancenormalizedkvcache/keybits.md)
- [var metaState: [String]](./variancenormalizedkvcache/metastate.md)
- [let sinkhornIterations: Int](./variancenormalizedkvcache/sinkhorniterations.md)
- [var state: [MLXArray]](./variancenormalizedkvcache/state.md)
- [let tileSize: Int](./variancenormalizedkvcache/tilesize.md)
- [let valueBits: Int](./variancenormalizedkvcache/valuebits.md)
### Instance Methods
- [func copy() -> any KVCache](./variancenormalizedkvcache/copy%28%29.md)
- [func innerState() -> [MLXArray]](./variancenormalizedkvcache/innerstate%28%29.md)
- [func isTrimmable(after: Int) -> Bool](./variancenormalizedkvcache/istrimmable%28after%29.md)
- [func trim(Int) -> Int](./variancenormalizedkvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./variancenormalizedkvcache/update%28keys,values%29.md)
- [func updateAndAttend(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode) -> MLXArray](./variancenormalizedkvcache/updateandattend%28queries,keys,values,scale,mask%29.md)
### Type Properties
- [class var serializedClassName: String?](./variancenormalizedkvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./variancenormalizedkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- [KVCacheAttentionProtocol](./kvcacheattentionprotocol.md)
- MLX.Evaluatable
- Swift.CustomDebugStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/variancenormalizedkvcache)*