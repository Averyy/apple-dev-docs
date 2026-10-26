---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcriptkvcache"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# TranscriptKVCache

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: class  
**Role**: Class

The tokens a model has processed, kept as an entry in its KV cache.

## Declaration

```swift
final class TranscriptKVCache
```

#### Overview

A scripted model appends this entry to its inner model’s caches and keeps it in step with them. Generation trims, rewinds, copies, and saves the whole cache together, so `tokens` always matches what the inner caches hold, across speculative rejections, prompt-cache reuse, and `ChatSession` rebuilds.

It is an `AuxiliaryKVCache`, so capacity and compression settings ignore it, and it never stores keys or values.

Note: this KVCache should not be used for any production use. Its performance is O(n^2) or worse and is strictly meant as a mechanism that a `ScriptedLogitsModel` could use.

## Topics

### Initializers
- [init(tokens: [Int])](./transcriptkvcache/init%28tokens%29.md)
### Instance Properties
- [var isTrimmable: Bool](./transcriptkvcache/istrimmable.md)
- [var metaState: [String]](./transcriptkvcache/metastate.md)
- [var state: [MLXArray]](./transcriptkvcache/state.md)
- [var tokens: [Int]](./transcriptkvcache/tokens.md)
### Instance Methods
- [func append([Int])](./transcriptkvcache/append%28_%29.md)
  Records tokens the inner model has just processed.
- [func copy() -> any KVCache](./transcriptkvcache/copy%28%29.md)
- [func trim(Int) -> Int](./transcriptkvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./transcriptkvcache/update%28keys,values%29.md)
### Type Properties
- [static var serializedClassName: String?](./transcriptkvcache/serializedclassname.md)
### Type Methods
- [static func register()](./transcriptkvcache/register%28%29.md)
  Register the type for KVCache save and restore. This will happen automatically if a cache instance is created.
- [static func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./transcriptkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- MLXLMCommon.BaseKVCache
### Conforms To
- MLX.Evaluatable
- MLXLMCommon.AuxiliaryKVCache
- MLXLMCommon.KVCache

## See Also

### Model Support
- [enum TranscriptKVCacheError](./transcriptkvcacheerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcriptkvcache)*