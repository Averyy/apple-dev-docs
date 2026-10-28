---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makepromptcache(model:parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makePromptCache(model:parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Construct the model’s cache for use when generating.

## Declaration

```swift
func makePromptCache(model: any LanguageModel, parameters: GenerateParameters? = nil) throws -> [KVCache]
```

## Discussion

This function will defer the cache construction to the model if it has a `newCache` method, otherwise it will make a default KV cache.

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request or a model-defined cache size is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makepromptcache(model:parameters:))*