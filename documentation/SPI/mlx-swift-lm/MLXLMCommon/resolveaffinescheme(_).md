---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolveaffinescheme(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolveAffineScheme(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Dynamically quantize KV caches during generation if conditions are met

## Declaration

```swift
func resolveAffineScheme(_ scheme: String?) -> (bits: Int, groupSize: Int)?
```

## Discussion

Resolve a kvScheme string to (bits, groupSize) for affine quantization. Returns nil for unrecognized schemes (custom schemes handle their own caches).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolveaffinescheme(_:))*