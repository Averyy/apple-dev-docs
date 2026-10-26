---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput/processedimage"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LMInput.ProcessedImage

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of prepared input image(s).

## Declaration

```swift
struct ProcessedImage
```

## Topics

### Initializers
- [init(pixels: MLXArray, positionIds: MLXArray?, frames: [THW]?)](./processedimage/init%28pixels,positionids,frames%29.md)
### Instance Properties
- [let frames: [THW]?](./processedimage/frames.md)
  Time, height, and width of the images
- [let pixels: MLXArray](./processedimage/pixels.md)
  Concatenated pixels from one or more images
- [let positionIds: MLXArray?](./processedimage/positionids.md)
  Optional per-patch position ids for encoder-free vision embedders.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput/processedimage)*