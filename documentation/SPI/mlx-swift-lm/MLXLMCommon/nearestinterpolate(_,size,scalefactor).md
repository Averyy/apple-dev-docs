---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nearestinterpolate(_:size:scalefactor:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# nearestInterpolate(_:size:scaleFactor:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Nearest neighbor interpolation using MLX Metal kernel.

## Declaration

```swift
func nearestInterpolate(_ x: MLXArray, size: (Int, Int)? = nil, scaleFactor: (Float, Float)? = nil) -> MLXArray
```

#### Return Value

Interpolated tensor of shape [B, C, outH, outW]

## Parameters

- `x`: Input tensor of shape [B, C, H, W]
- `size`: Target output size (outH, outW). Either this or scaleFactor must be provided.
- `scaleFactor`: Scale factor as a single value or tuple (scaleH, scaleW). Either this or size must be provided.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nearestinterpolate(_:size:scalefactor:))*