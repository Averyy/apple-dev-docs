---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RotatingKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Rotating KV cache for sliding window attention

## Declaration

```swift
class RotatingKVCache
```

## Topics

### Initializers
- [init(maxSize: Int, keep: Int, step: Int, rewindCapacity: Int)](./rotatingkvcache/init%28maxsize,keep,step,rewindcapacity%29.md)
### Instance Properties
- [var debugDescription: String](./rotatingkvcache/debugdescription.md)
- [var evictedTokenCount: Int](./rotatingkvcache/evictedtokencount.md)
- [var isTrimmable: Bool](./rotatingkvcache/istrimmable.md)
- [var maxSize: Int?](./rotatingkvcache/maxsize.md)
- [var maxTrimCount: Int](./rotatingkvcache/maxtrimcount.md)
- [var metaState: [String]](./rotatingkvcache/metastate.md)
- [var rewindCapacity: Int](./rotatingkvcache/rewindcapacity.md)
  Additional historical rows retained for exact prefix rewinds. The attention window remains [`maxSize`](./rotatingkvcache/maxsize.md). Zero preserves the usual memory bound.
- [var state: [MLXArray]](./rotatingkvcache/state.md)
### Instance Methods
- [func copy() -> any KVCache](./rotatingkvcache/copy%28%29.md)
- [func innerState() -> [MLXArray]](./rotatingkvcache/innerstate%28%29.md)
- [func isTrimmable(after: Int) -> Bool](./rotatingkvcache/istrimmable%28after%29.md)
- [func makeMask(n: Int, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./rotatingkvcache/makemask%28n,windowsize,returnarray%29.md)
  Optimized mask creation for rotating cache with offset capping
- [func toQuantized(groupSize: Int, bits: Int) throws -> QuantizedKVCache](./rotatingkvcache/toquantized%28groupsize,bits%29.md)
  Convert to a quantized cache.
- [func trim(Int) -> Int](./rotatingkvcache/trim%28_%29.md)
  Rewind the newest `n` positions.
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./rotatingkvcache/update%28keys,values%29.md)
### Type Properties
- [class var serializedClassName: String?](./rotatingkvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./rotatingkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable
- Swift.CustomDebugStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache)*