---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadpromptcachesnapshot(url:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadPromptCacheSnapshot(url:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a prompt cache and its associated model state from a file.

## Declaration

```swift
func loadPromptCacheSnapshot(url: URL) throws -> PromptCacheSnapshot
```

## Discussion

The arrays are read before this returns, so the file can be overwritten or removed afterwards.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadpromptcachesnapshot(url:))*