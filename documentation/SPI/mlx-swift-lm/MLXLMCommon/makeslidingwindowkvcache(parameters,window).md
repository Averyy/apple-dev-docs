---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeslidingwindowkvcache(parameters:window:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeSlidingWindowKVCache(parameters:window:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Architecture-imposed sliding-window attention cache, capped by legacy `maxKVSize`.

## Declaration

```swift
func makeSlidingWindowKVCache(parameters: GenerateParameters?, window: Int) throws -> KVCache
```

#### Discussion

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request or window is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeslidingwindowkvcache(parameters:window:))*