---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Implementation of KV cache functionality for MLX Swift

## Declaration

```swift
protocol KVCache : Evaluatable
```

## Mentions

- [Developing mlx-swift-lm](./developing.md)

#### Quantized Cache Usage

**Standard caches:**

```swift
let cache = KVCacheSimple()
let (keys, values) = cache.update(keys: keys, values: values)
let output = MLXFast.scaledDotProductAttention(queries: q, keys: keys, values: values, ...)
```

**Quantized cache:**

```swift
let quantizedCache = QuantizedKVCache(groupSize: 64, bits: 4)
let (qKeys, qValues) = quantizedCache.updateQuantized(keys: keys, values: values)

let output = quantizedScaledDotProductAttention(
    queries: queries,
    quantizedKeys: qKeys,
    quantizedValues: qValues,
    scale: scale,
    mask: mask,
    groupSize: quantizedCache.groupSize,
    bits: quantizedCache.bits
)
```

Interface for Key/Value cache for LLMs.

See [`newCache(parameters:)`](./languagemodel/newcache%28parameters%29.md)

## Topics

### Instance Properties
- [var evictedTokenCount: Int](./kvcache/evictedtokencount.md)
  Number of historical positions this cache no longer retains.
- [var isTrimmable: Bool](./kvcache/istrimmable.md)
  whether this cache can be trimmed
- [var maxSize: Int?](./kvcache/maxsize.md)
  get the maximum size (if any)
- [var maxTrimCount: Int](./kvcache/maxtrimcount.md)
  Maximum number of newest positions that can be removed with an exact rewind.
- [var metaState: [String]](./kvcache/metastate.md)
  get/set metadata state as string array for serialization
- [var offset: Int](./kvcache/offset.md)
  get the current offset
- [var ropeOffset: RoPEOffset](./kvcache/ropeoffset.md)
  Offset to use with [`applyRotaryPosition(_:to:offset:)`](./applyrotaryposition%28_,to,offset%29.md).
- [var state: [MLXArray]](./kvcache/state.md)
  get the current state for serialization
### Instance Methods
- [func copy() -> any KVCache](./kvcache/copy%28%29.md)
  Create an independent deep copy of this cache.
- [func finalize()](./kvcache/finalize%28%29.md)
  Clear transient cache metadata after generation.
- [func isTrimmable(after: Int) -> Bool](./kvcache/istrimmable%28after%29.md)
  Predict whether this cache can still be trimmed after appending `positions`.
- [func makeMask(n: Int, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./kvcache/makemask%28n,windowsize,returnarray%29.md)
  Create an attention mask for this cache
- [func prepare(lengths: MLXArray?)](./kvcache/prepare%28lengths%29-7u4kg.md)
  Prepare cache metadata for a batched sequence.
- [func prepare(lengths: [Int]?)](./kvcache/prepare%28lengths%29-9d6e1.md)
  Prepare cache metadata for a batched sequence.
- [func trim(Int) -> Int](./kvcache/trim%28_%29.md)
  trim n tokens from the cache, returning actual number trimmed
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./kvcache/update%28keys,values%29.md)
  update the cache with new keys and values and return all keys/values
### Type Properties
- [static var serializedClassName: String?](./kvcache/serializedclassname.md)
  The class name written to prompt cache files, or `nil` if this cache cannot be saved.
### Type Methods
- [static func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./kvcache/restore%28state,metastate%29.md)
  Rebuild a cache from the `state` and `metaState` it saved.

## Relationships

### Inherits From
- MLX.Evaluatable
### Inherited By
- [AuxiliaryKVCache](./auxiliarykvcache.md)
- [BatchPositionedKVCache](./batchpositionedkvcache.md)
- [KVCacheAttentionProtocol](./kvcacheattentionprotocol.md)
- [QuantizedKVCacheProtocol](./quantizedkvcacheprotocol.md)
### Conforming Types
- [ArraysCache](./arrayscache.md)
- [BaseKVCache](./basekvcache.md)
- [CacheList](./cachelist.md)
- [ChunkedKVCache](./chunkedkvcache.md)
- [KVCacheSimple](./kvcachesimple.md)
- [MambaCache](./mambacache.md)
- [QuantizedKVCache](./quantizedkvcache.md)
- [RotatingKVCache](./rotatingkvcache.md)
- [TurboQuantKVCache](./turboquantkvcache.md)
- [VarianceNormalizedKVCache](./variancenormalizedkvcache.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache)*