---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/videoprocessing"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput.VideoProcessing

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of video processing options.

## Declaration

```swift
struct VideoProcessing
```

## Topics

### Initializers
- [init(sampling: SamplingMethod?)](./videoprocessing/init%28sampling%29.md)
- [init(targetFrames: Int)](./videoprocessing/init%28targetframes%29.md)
  Convenience initializer to sample a fixed number of frames across the video.
- [init(targetFramesPerSecond: Double)](./videoprocessing/init%28targetframespersecond%29.md)
  Convenience initializer to target a sampling density in frames per second.
### Instance Properties
- [var sampling: SamplingMethod?](./videoprocessing/sampling.md)
  The sampling strategy to use, or `nil` to use model default behavior.
- [var targetFrames: Int?](./videoprocessing/targetframes.md)
  Target number of frames to sample from the video, regardless of duration.
- [var targetFramesPerSecond: Double?](./videoprocessing/targetframespersecond.md)
  Target frame rate (frames per second) to sample from the video.
### Enumerations
- [UserInput.VideoProcessing.SamplingMethod](./videoprocessing/samplingmethod.md)
  Strategy for temporal frame sampling.
### Default Implementations
- [Equatable Implementations](./videoprocessing/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/videoprocessing)*