---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/promptcachesnapshot/init(cache:metadata:state:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(cache:metadata:state:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Pair a cache with the model state that belongs with it.

## Declaration

```swift
init(cache: [KVCache], metadata: [String : String] = [:], state: LMOutput.State? = nil)
```

## Discussion

Use this when the cache was built in process — [`loadPromptCacheSnapshot(url:)`](../loadpromptcachesnapshot%28url%29.md) returns a snapshot for caches read from disk.

## Parameters

- `cache`: The KV cache
- `metadata`: Optional caller metadata to carry alongside it
- `state`: The model state captured with the cache, if the model produced any


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/promptcachesnapshot/init(cache:metadata:state:))*