---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/cachestatus(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# cacheStatus(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Authoritative planned status of the cache [`newCache(parameters:)`](./newcache%28parameters%29.md) produces.

## Declaration

```swift
func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus
```

## Mentions

- [KV Cache Quantization](../kv-cache-quantization.md)

#### Discussion

Use this from [`ModelContainer`](../modelcontainer.md) / [`ChatSession`](../chatsession.md) (or directly on the model) to inspect topology, requested capacity, and strategy compatibility without allocating or casting probe caches in application code.

The default implementation derives the description from [`newCache(parameters:)`](./newcache%28parameters%29.md). Models may override with a zero-allocation declarative path, but must stay consistent with [`newCache(parameters:)`](./newcache%28parameters%29.md).

## Default Implementations

### LanguageModel Implementations
- [func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus](./cachestatus%28parameters%29-3s3eo.md)
  Default: classify the caches that [`newCache(parameters:)`](./newcache%28parameters%29.md) constructs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/cachestatus(parameters:))*