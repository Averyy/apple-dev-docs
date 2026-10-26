---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/basekvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Base cache implementation providing default behaviors

## Declaration

```swift
class BaseKVCache
```

## Topics

### Initializers
- [init()](./basekvcache/init%28%29.md)
### Instance Properties
- [var evictedTokenCount: Int](./basekvcache/evictedtokencount.md)
- [var isTrimmable: Bool](./basekvcache/istrimmable.md)
- [var maxSize: Int?](./basekvcache/maxsize.md)
- [var maxTrimCount: Int](./basekvcache/maxtrimcount.md)
- [var metaState: [String]](./basekvcache/metastate.md)
- [var offset: Int](./basekvcache/offset.md)
- [var ropeOffset: RoPEOffset](./basekvcache/ropeoffset.md)
  RoPE offset for this cache. `open` so subclasses can return a non-scalar offset (e.g. a batched cache’s per-row `.batch(...)`).
- [var state: [MLXArray]](./basekvcache/state.md)
### Instance Methods
- [func copy() -> any KVCache](./basekvcache/copy%28%29.md)
- [func finalize()](./basekvcache/finalize%28%29.md)
- [func innerState() -> [MLXArray]](./basekvcache/innerstate%28%29.md)
- [func isTrimmable(after: Int) -> Bool](./basekvcache/istrimmable%28after%29.md)
- [func makeMask(n: Int, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./basekvcache/makemask%28n,windowsize,returnarray%29.md)
  Default implementation for caches without special mask requirements
- [func prepare(lengths: MLXArray?)](./basekvcache/prepare%28lengths%29-6dszo.md)
- [func prepare(lengths: [Int]?)](./basekvcache/prepare%28lengths%29-8m9v7.md)
- [func trim(Int) -> Int](./basekvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./basekvcache/update%28keys,values%29.md)
### Type Properties
- [class var serializedClassName: String?](./basekvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./basekvcache/restore%28state,metastate%29.md)
### Default Implementations
- [KVCache Implementations](./basekvcache/kvcache-implementations.md)

## Relationships

### Inherited By
- [ArraysCache](./arrayscache.md)
- [CacheList](./cachelist.md)
- [KVCacheSimple](./kvcachesimple.md)
- [QuantizedKVCache](./quantizedkvcache.md)
- [RotatingKVCache](./rotatingkvcache.md)
- [TurboQuantKVCache](./turboquantkvcache.md)
- [VarianceNormalizedKVCache](./variancenormalizedkvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/basekvcache)*