---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asmlxarray(_:colorspace:)"
framework: "mlx-swift-lm/MLXVLM"
---

# asMLXArray(_:colorSpace:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

Convert the CIImage into a planar 3 channel MLXArray `[1, C, H, W]`

## Declaration

```swift
static func asMLXArray(_ image: CIImage, colorSpace: CGColorSpace? = nil) -> MLXArray
```

## Return Value

The MLXArray representation of the image

## Parameters

- `image`: The image to convert
- `colorSpace`: Optional color space for rendering


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asmlxarray(_:colorspace:))*