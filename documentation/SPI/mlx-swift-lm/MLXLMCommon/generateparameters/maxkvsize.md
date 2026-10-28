---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/maxkvsize"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maxKVSize

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Maximum size of the key-value cache. Old entries are overwritten while retaining up to the first 4 tokens when the requested size permits. The value must be greater than zero; generation and cache construction throw [`KVCacheConfigurationError.invalidCapacity(_:)`](../kvcacheconfigurationerror/invalidcapacity%28_%29.md) for an invalid value.

## Declaration

```swift
var maxKVSize: Int?
```

## Discussion

When set, full-attention layers that would otherwise use [`KVCacheSimple`](../kvcachesimple.md) use [`RotatingKVCache`](../rotatingkvcache.md) instead. Architecture sliding-window layers use the smaller of their model-defined window and this limit. State-space / Mamba / GDN layers are not token-windowed and therefore do not consume this budget.

Inspect the effective policy with [`cacheStatus(parameters:)`](../languagemodel/cachestatus%28parameters%29.md) (also on [`ModelContainer`](../modelcontainer.md) / [`ChatSession`](../chatsession.md)). This is a cache policy, not a generation stop reason — output token limits still surface as [`GenerateStopReason.length`](../generatestopreason/length.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/maxkvsize)*