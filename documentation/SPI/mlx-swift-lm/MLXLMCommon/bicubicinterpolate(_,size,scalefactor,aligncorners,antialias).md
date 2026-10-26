---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/bicubicinterpolate(_:size:scalefactor:aligncorners:antialias:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# bicubicInterpolate(_:size:scaleFactor:alignCorners:antialias:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Bicubic interpolation using MLX Metal kernel.

## Declaration

```swift
func bicubicInterpolate(_ x: MLXArray, size: (Int, Int)? = nil, scaleFactor: (Float, Float)? = nil, alignCorners: Bool = false, antialias: Bool = false) -> MLXArray
```

#### Return Value

Interpolated tensor of shape [B, C, outH, outW]

## Parameters

- `x`: Input tensor of shape [B, C, H, W]
- `size`: Target output size (outH, outW). Either this or scaleFactor must be provided.
- `scaleFactor`: Scale factor as a single value or tuple (scaleH, scaleW). Either this or size must be provided.
- `alignCorners`: Whether to align corners during interpolation.
- `antialias`: Whether to apply antialiasing (useful when downsampling).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/bicubicinterpolate(_:size:scalefactor:aligncorners:antialias:))*