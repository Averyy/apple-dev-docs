---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/registerkvcachetype(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# registerKVCacheType(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Register a cache type so [`loadPromptCacheSnapshot(url:)`](./loadpromptcachesnapshot%28url%29.md) can restore it.

## Declaration

```swift
func registerKVCacheType<T>(_ type: T.Type) throws where T : KVCache
```

## Discussion

[`savePromptCache(url:cache:metadata:state:)`](./savepromptcache%28url,cache,metadata,state%29.md) registers the types it writes, so a file saved and loaded in one process works without this call. Call it before loading in a new process. Registering the same type again has no effect.

> **Throws**: If the type has no [`serializedClassName`](./kvcache/serializedclassname.md), or another type already uses it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/registerkvcachetype(_:))*