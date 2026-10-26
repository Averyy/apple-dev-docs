---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvevariancenormalizedscheme(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolveVarianceNormalizedScheme(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Resolve a legacy `kvScheme` string for variance-normalized compression.

## Declaration

```swift
func resolveVarianceNormalizedScheme(_ scheme: String?) -> (keyBits: Int, valueBits: Int, tileSize: Int, sinkhornIterations: Int)?
```

#### Discussion

Supported schemes:

- `"varn"` / `"varn4v2"`: 4-bit keys, 2-bit values, 128-token tiles
- `"varn4"` / `"varn4v4"`: 4-bit keys and values
- `"varn2"` / `"varn2v2"`: 2-bit keys and values
- `"varn4v2t32"` / `"varn4v2t64"` / `"varn4v2t128"`: explicit tile size


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvevariancenormalizedscheme(_:))*