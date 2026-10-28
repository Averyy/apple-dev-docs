---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/bicubicinterpolate(_:scalefactor:aligncorners:antialias:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# bicubicInterpolate(_:scaleFactor:alignCorners:antialias:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Bicubic interpolation with a single scale factor.

## Declaration

```swift
func bicubicInterpolate(_ x: MLXArray, scaleFactor: Float, alignCorners: Bool = false, antialias: Bool = false) -> MLXArray
```

## Return Value

Interpolated tensor of shape [B, C, outH, outW]

## Parameters

- `x`: Input tensor of shape [B, C, H, W]
- `scaleFactor`: Single scale factor applied to both dimensions.
- `alignCorners`: Whether to align corners during interpolation.
- `antialias`: Whether to apply antialiasing.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/bicubicinterpolate(_:scalefactor:aligncorners:antialias:))*