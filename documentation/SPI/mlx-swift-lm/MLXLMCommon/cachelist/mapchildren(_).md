---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist/mapchildren(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mapChildren(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Recursively apply a transformation to every non-composite child cache.

## Declaration

```swift
func mapChildren(_ transform: (KVCache) -> KVCache)
```

## Discussion

`CacheList` children are descended into; any other cache is passed to `transform` and replaced by the returned value. This is the primitive used by dynamic cache quantization and other cache-wide rewrites for models with hybrid attention/recurrent caches (e.g. Falcon-H1).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist/mapchildren(_:))*