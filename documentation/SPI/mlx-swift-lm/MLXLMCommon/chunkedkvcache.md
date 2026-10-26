---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chunkedkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChunkedKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Chunked KV cache for processing large contexts in chunks

## Declaration

```swift
class ChunkedKVCache
```

## Topics

### Initializers
- [init(chunkSize: Int?)](./chunkedkvcache/init%28chunksize%29.md)
### Instance Properties
- [var metaState: [String]](./chunkedkvcache/metastate.md)
### Instance Methods
- [func copy() -> any KVCache](./chunkedkvcache/copy%28%29.md)
- [func maybeTrimFront()](./chunkedkvcache/maybetrimfront%28%29.md)
- [func trim(Int) -> Int](./chunkedkvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./chunkedkvcache/update%28keys,values%29.md)
### Type Properties
- [class var serializedClassName: String?](./chunkedkvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./chunkedkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [KVCacheSimple](./kvcachesimple.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable
- Swift.CustomDebugStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chunkedkvcache)*