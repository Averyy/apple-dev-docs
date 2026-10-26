---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/savepromptcache(url:cache:metadata:state:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# savePromptCache(url:cache:metadata:state:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Save a pre-computed prompt cache to a file.

## Declaration

```swift
func savePromptCache(url: URL, cache: [KVCache], metadata: [String : String] = [:], state: LMOutput.State? = nil) throws
```

## Parameters

- `url`: The URL to the `.safetensors` file
- `cache`: The model cache state
- `metadata`: Optional metadata to save along with cache state
- `state`: Optional model state associated with the cache


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/savepromptcache(url:cache:metadata:state:))*