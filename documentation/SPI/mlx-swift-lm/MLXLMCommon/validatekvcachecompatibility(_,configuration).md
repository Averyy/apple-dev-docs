---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/validatekvcachecompatibility(_:configuration:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# validateKVCacheCompatibility(_:configuration:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Validate the requested compatibility policy against a concrete model cache.

## Declaration

```swift
func validateKVCacheCompatibility(_ cache: [KVCache], configuration: KVCacheConfiguration) throws
```

## Discussion

Full-precision and non-attention state entries do not participate. Affine caches are accepted for TurboQuant because aggressive configurations use them as an intentional boundary-layer fallback.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/validatekvcachecompatibility(_:configuration:))*