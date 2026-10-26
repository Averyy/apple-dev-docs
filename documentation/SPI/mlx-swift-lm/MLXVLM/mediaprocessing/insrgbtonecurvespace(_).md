---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/insrgbtonecurvespace(_:)"
framework: "mlx-swift-lm/MLXVLM"
---

# inSRGBToneCurveSpace(_:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

VLM media processing is normally done without regard to the colorspace. Many, though not all, images are stored in sRGB and this will be the implicit colorspace used. This converts to a colorspace with an sRGB tone curve, though not necessarily sRGB primaries, etc.

## Declaration

```swift
static func inSRGBToneCurveSpace(_ image: CIImage) -> CIImage
```

#### Discussion

See [`inLinearToneCurveSpace(_:)`](./inlineartonecurvespace%28_%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/insrgbtonecurvespace(_:))*