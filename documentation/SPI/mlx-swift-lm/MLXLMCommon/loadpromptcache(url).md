---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadpromptcache(url:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadPromptCache(url:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a prompt cache from a file, without model state.

## Declaration

```swift
func loadPromptCache(url: URL) throws -> ([KVCache], [String : String])
```

## Return Value

The prompt cache and the metadata

## Discussion

Prefer [`loadPromptCacheSnapshot(url:)`](./loadpromptcachesnapshot%28url%29.md), which also restores the model state a cache needs to be continued correctly. This tuple form has no slot for that state, so it rejects files that carry any rather than dropping it. Models that position from a carried anchor refuse a warm cache that arrives without one, so a cache saved through this API cannot warm them.

> **Throws**: If the file contains model state that this tuple return value cannot represent

## Parameters

- `url`: The URL to the `.safetensors` file


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadpromptcache(url:))*