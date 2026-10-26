---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachesimple"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheSimple

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Standard KV cache implementation based on Python’s KVCache See https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/models/base.py#L11

## Declaration

```swift
class KVCacheSimple
```

## Topics

### Initializers
- [init()](./kvcachesimple/init%28%29.md)
### Instance Properties
- [var debugDescription: String](./kvcachesimple/debugdescription.md)
- [var isTrimmable: Bool](./kvcachesimple/istrimmable.md)
- [var state: [MLXArray]](./kvcachesimple/state.md)
- [var step: Int](./kvcachesimple/step.md)
### Instance Methods
- [func copy() -> any KVCache](./kvcachesimple/copy%28%29.md)
- [func innerState() -> [MLXArray]](./kvcachesimple/innerstate%28%29.md)
- [func toQuantized(groupSize: Int, bits: Int) throws -> QuantizedKVCache](./kvcachesimple/toquantized%28groupsize,bits%29.md)
  Convert to a quantized cache for maximum efficiency.
- [func toVarianceNormalized(tileSize: Int, keyBits: Int, valueBits: Int, sinkhornIterations: Int) -> VarianceNormalizedKVCache](./kvcachesimple/tovariancenormalized%28tilesize,keybits,valuebits,sinkhorniterations%29.md)
  Convert to a variance-normalized tile cache.
- [func trim(Int) -> Int](./kvcachesimple/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./kvcachesimple/update%28keys,values%29.md)
### Type Properties
- [class var serializedClassName: String?](./kvcachesimple/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./kvcachesimple/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Inherited By
- [ChunkedKVCache](./chunkedkvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable
- Swift.CustomDebugStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachesimple)*