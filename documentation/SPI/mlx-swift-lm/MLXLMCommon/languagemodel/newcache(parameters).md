---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/newcache(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# newCache(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Create a new array of [`KVCache`](../kvcache.md) appropriate for this model.

## Declaration

```swift
func newCache(parameters: GenerateParameters?) throws -> [KVCache]
```

## Discussion

Implementations must honor [`maxKVSize`](../generateparameters/maxkvsize.md) for any attention layer that can be token-windowed. Hybrid attention / state-space models apply the limit to attention caches only (see [`makeAttentionKVCache(parameters:)`](../makeattentionkvcache%28parameters%29.md)).

> **Throws**: [`KVCacheConfigurationError`](../kvcacheconfigurationerror.md) when the request or a model-defined cache size is invalid.

Automatic implementation if self implements [`KVCacheDimensionProvider`](../kvcachedimensionprovider.md).

## Default Implementations

### LanguageModel Implementations
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./newcache%28parameters%29-2cxt.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/newcache(parameters:))*