---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makepromptcachewithlayercount(numlayers:maxkvsize:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makePromptCacheWithLayerCount(numLayers:maxKVSize:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Fallback function to create cache when layer count is known

## Declaration

```swift
func makePromptCacheWithLayerCount(numLayers: Int, maxKVSize: Int? = nil) throws -> [KVCache]
```

#### Discussion

This function creates a default cache structure when the number of layers is known. Use this when `makePromptCache` cannot determine the layer count automatically.

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when `maxKVSize` is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makepromptcachewithlayercount(numlayers:maxkvsize:))*