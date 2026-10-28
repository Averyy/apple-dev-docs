---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeattentionkvcache(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeAttentionKVCache(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Build a standard full-attention [`KVCache`](./kvcache.md) that honors the requested capacity.

## Declaration

```swift
func makeAttentionKVCache(parameters: GenerateParameters?) throws -> KVCache
```

## Discussion

> **Throws**: [`KVCacheConfigurationError`](./kvcacheconfigurationerror.md) when the request is invalid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeattentionkvcache(parameters:))*