---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/arrayscache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ArraysCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Base cache for array-based state storage

## Declaration

```swift
class ArraysCache
```

## Topics

### Initializers
- [init(size: Int, leftPadding: [Int]?)](./arrayscache/init%28size,leftpadding%29.md)
### Instance Properties
- [var currentLengths: MLXArray?](./arrayscache/currentlengths.md)
- [var metaState: [String]](./arrayscache/metastate.md)
  metaState format: [slotCount, presentSlots, leftPadding?, lengths?] Legacy format (BaseKVCache default): [””]
- [var state: [MLXArray]](./arrayscache/state.md)
### Instance Methods
- [func advance(Int)](./arrayscache/advance%28_%29.md)
- [func copy() -> any KVCache](./arrayscache/copy%28%29.md)
- [func extend(other: ArraysCache)](./arrayscache/extend%28other%29.md)
  In-place extend this cache with the other cache
- [func filter(batchIndices: MLXArray)](./arrayscache/filter%28batchindices%29.md)
  In-place filter to keep just the given indices in the cache
- [func finalize()](./arrayscache/finalize%28%29.md)
- [func innerState() -> [MLXArray]](./arrayscache/innerstate%28%29.md)
- [func makeMask(N: Int) -> MLXArray?](./arrayscache/makemask%28n%29.md)
  Create attention mask based on left padding or prepared sequence lengths
- [func prepare(lengths: MLXArray?)](./arrayscache/prepare%28lengths%29-6nqug.md)
- [func prepare(lengths: [Int]?)](./arrayscache/prepare%28lengths%29-6ox2r.md)
### Subscripts
- [subscript(Int) -> MLXArray?](./arrayscache/subscript%28_%29.md)
### Type Properties
- [class var serializedClassName: String?](./arrayscache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./arrayscache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Inherited By
- [MambaCache](./mambacache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/arrayscache)*