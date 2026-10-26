---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolveturboscheme(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolveTurboScheme(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Resolve a TurboQuant kvScheme string to (keyBits, valueBits). `keyBits == 0` means raw FP16 keys (only values are compressed). Returns nil for non-TurboQuant schemes.

## Declaration

```swift
func resolveTurboScheme(_ scheme: String?) -> (keyBits: Int, valueBits: Int)?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolveturboscheme(_:))*