---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/videoprocessing/samplingmethod"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput.VideoProcessing.SamplingMethod

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Strategy for temporal frame sampling.

## Declaration

```swift
enum SamplingMethod
```

## Topics

### Enumeration Cases
- [UserInput.VideoProcessing.SamplingMethod.framesPerSecond(_:)](./samplingmethod/framespersecond%28_%29.md)
  Derive a target frame count from frames per second, then distribute those frames evenly across the video duration.
- [UserInput.VideoProcessing.SamplingMethod.targetFrames(_:)](./samplingmethod/targetframes%28_%29.md)
  Sample a fixed total count of frames distributed evenly across the video duration.
### Default Implementations
- [Equatable Implementations](./samplingmethod/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/videoprocessing/samplingmethod)*