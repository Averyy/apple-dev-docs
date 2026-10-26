---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpcachecheckpointindexkey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpCacheCheckpointIndexKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

Requests a recurrent-cache checkpoint after this many verification input tokens. Hybrid Qwen models use `1` for MTP-1 so a rejected draft restores state after the always-committed bonus token without replaying the model.

## Declaration

```swift
let mtpCacheCheckpointIndexKey: LMOutput.Key<Int>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpcachecheckpointindexkey)*