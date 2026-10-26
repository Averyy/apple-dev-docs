---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applykvcacheconfiguration(cache:configuration:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# applyKVCacheConfiguration(cache:configuration:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Apply a typed cache strategy to every eligible cache layer.

## Declaration

```swift
func applyKVCacheConfiguration(cache: inout [KVCache], configuration: KVCacheConfiguration) throws -> KVCacheApplicationResult
```

#### Discussion

This is the single runtime dispatch point used by autoregressive, speculative, guided, and diagnostic generation paths.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applykvcacheconfiguration(cache:configuration:))*