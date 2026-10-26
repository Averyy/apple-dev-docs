---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/slidingwindowcachekind(parameters:window:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# slidingWindowCacheKind(parameters:window:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Architecture-imposed sliding-window attention kind, capped by legacy `maxKVSize`.

## Declaration

```swift
func slidingWindowCacheKind(parameters: GenerateParameters?, window: Int) throws -> CacheLayerKind
```

#### Discussion

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request or window is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/slidingwindowcachekind(parameters:window:))*