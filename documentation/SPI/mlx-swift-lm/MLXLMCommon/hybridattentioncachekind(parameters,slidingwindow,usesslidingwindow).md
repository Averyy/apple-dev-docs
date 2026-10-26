---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/hybridattentioncachekind(parameters:slidingwindow:usesslidingwindow:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# hybridAttentionCacheKind(parameters:slidingWindow:usesSlidingWindow:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Full-attention kind if the layer is not sliding-window; otherwise the architecture sliding window capped by legacy `maxKVSize`.

## Declaration

```swift
func hybridAttentionCacheKind(parameters: GenerateParameters?, slidingWindow: Int?, usesSlidingWindow: Bool) throws -> CacheLayerKind
```

#### Discussion

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request or window is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/hybridattentioncachekind(parameters:slidingwindow:usesslidingwindow:))*