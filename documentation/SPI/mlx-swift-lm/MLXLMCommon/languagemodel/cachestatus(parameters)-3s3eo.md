---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/cachestatus(parameters:)-3s3eo"
framework: "mlx-swift-lm/MLXLMCommon"
---

# cacheStatus(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Default: classify the caches that [`newCache(parameters:)`](./newcache%28parameters%29.md) constructs.

## Declaration

```swift
func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus
```

## Discussion

Empty caches allocate negligible state (no tensors until the first update), so this is always consistent with the runtime path. Prefer a declarative override only when construction itself is expensive.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/cachestatus(parameters:)-3s3eo)*