---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CacheList

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Composite cache that manages multiple sub-caches

## Declaration

```swift
class CacheList
```

## Topics

### Initializers
- [init(KVCache...)](./cachelist/init%28_%29.md)
### Instance Properties
- [var evictedTokenCount: Int](./cachelist/evictedtokencount.md)
- [var isTrimmable: Bool](./cachelist/istrimmable.md)
- [var maxTrimCount: Int](./cachelist/maxtrimcount.md)
- [var metaState: [String]](./cachelist/metastate.md)
  metaState format: [childCount, (className, stateCount, metaStateCount, …metaState)*]
- [var state: [MLXArray]](./cachelist/state.md)
### Instance Methods
- [func copy() -> any KVCache](./cachelist/copy%28%29.md)
- [func finalize()](./cachelist/finalize%28%29.md)
- [func innerState() -> [MLXArray]](./cachelist/innerstate%28%29.md)
- [func isTrimmable(after: Int) -> Bool](./cachelist/istrimmable%28after%29.md)
- [func mapChildren((KVCache) -> KVCache)](./cachelist/mapchildren%28_%29.md)
  Recursively apply a transformation to every non-composite child cache.
- [func prepare(lengths: [Int]?)](./cachelist/prepare%28lengths%29-1yvmb.md)
- [func prepare(lengths: MLXArray?)](./cachelist/prepare%28lengths%29-7cfot.md)
- [func trim(Int) -> Int](./cachelist/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./cachelist/update%28keys,values%29.md)
### Subscripts
- [subscript(Int) -> KVCache](./cachelist/subscript%28_%29.md)
### Type Properties
- [class var serializedClassName: String?](./cachelist/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./cachelist/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist)*