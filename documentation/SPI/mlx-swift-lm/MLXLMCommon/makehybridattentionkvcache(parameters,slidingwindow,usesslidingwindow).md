---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makehybridattentionkvcache(parameters:slidingwindow:usesslidingwindow:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeHybridAttentionKVCache(parameters:slidingWindow:usesSlidingWindow:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Full-attention cache if the layer is not sliding-window; otherwise the architecture sliding window capped by legacy `maxKVSize`.

## Declaration

```swift
func makeHybridAttentionKVCache(parameters: GenerateParameters?, slidingWindow: Int?, usesSlidingWindow: Bool) throws -> KVCache
```

## Discussion

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request or window is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makehybridattentionkvcache(parameters:slidingwindow:usesslidingwindow:))*