---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nearestinterpolate(_:scalefactor:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# nearestInterpolate(_:scaleFactor:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Nearest neighbor interpolation with a single scale factor.

## Declaration

```swift
func nearestInterpolate(_ x: MLXArray, scaleFactor: Float) -> MLXArray
```

## Return Value

Interpolated tensor of shape [B, C, outH, outW]

## Parameters

- `x`: Input tensor of shape [B, C, H, W]
- `scaleFactor`: Single scale factor applied to both dimensions.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nearestinterpolate(_:scalefactor:))*