---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel/requiressharedtargetkv"
framework: "mlx-swift-lm/MLXLMCommon"
---

# requiresSharedTargetKV

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Whether this drafter consumes target-emitted shared K/V. Qwen owns a private full-attention cache and therefore only needs target hidden states; Gemma-style assistants consume the shared target K/V directly.

## Declaration

```swift
var requiresSharedTargetKV: Bool { get }
```

## Default Implementations

### MTPDrafterModel Implementations
- [var requiresSharedTargetKV: Bool](./requiressharedtargetkv-7fkos.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel/requiressharedtargetkv)*