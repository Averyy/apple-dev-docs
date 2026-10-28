---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/attentioncachekind(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# attentionCacheKind(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Build a standard full-attention cache kind that honors the requested capacity.

## Declaration

```swift
func attentionCacheKind(parameters: GenerateParameters?) throws -> CacheLayerKind
```

## Discussion

The capacity is the unified view of [`maxKVSize`](./generateparameters/maxkvsize.md) and the capacity carried by [`kvCache`](./generateparameters/kvcache.md).

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/attentioncachekind(parameters:))*