---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/savecache(to:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# saveCache(to:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Saves the current KV cache to disk.

## Declaration

```swift
func saveCache(to url: URL) async throws
```

#### Discussion

Use [`loadPromptCacheSnapshot(url:)`](../loadpromptcachesnapshot%28url%29.md) and an initializer that accepts a `promptCache` to restore the saved cache and model state in a future session.

> ❗ **Important**: This saves raw KV state only. It does not save the structured transcript retained by `ChatSession`. A restored raw cache therefore uses fragment-based continuation and is not suitable for conversation-aware structured tool continuations. Persist the messages separately and restore them with a history initializer when the transcript is required.

> **Throws**: [`ChatSessionError.noCacheAvailable`](../chatsessionerror/nocacheavailable.md) if no generation has occurred yet, or any error thrown by the underlying file write

## Parameters

- `url`: The file URL to write the cache to


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/savecache(to:))*