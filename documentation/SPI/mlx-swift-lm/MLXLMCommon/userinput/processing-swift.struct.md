---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/processing-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput.Processing

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of processing to apply to media.

## Declaration

```swift
struct Processing
```

## Topics

### Initializers
- [init(resize: CGSize?, video: VideoProcessing, audio: AudioProcessing, minPixels: Int?, maxPixels: Int?)](./processing-swift.struct/init%28resize,video,audio,minpixels,maxpixels%29.md)
### Instance Properties
- [var audio: UserInput.AudioProcessing](./processing-swift.struct/audio.md)
- [var maxPixels: Int?](./processing-swift.struct/maxpixels.md)
- [var minPixels: Int?](./processing-swift.struct/minpixels.md)
  Optional per-call overrides for the image resize budget. When set, they replace the model’s configured `min_pixels` / `max_pixels` for this request; when `nil` the model configuration is used. This lets a caller request the resolution a model was tuned for without hard-coding pixel counts in the processor.
- [var resize: CGSize?](./processing-swift.struct/resize.md)
- [var video: UserInput.VideoProcessing](./processing-swift.struct/video.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/processing-swift.struct)*