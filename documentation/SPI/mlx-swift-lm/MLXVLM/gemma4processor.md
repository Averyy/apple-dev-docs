---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processor"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4Processor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Gemma4Processor
```

## Topics

### Initializers
- [init(Gemma4ProcessorConfiguration, tokenizer: any Tokenizer)](./gemma4processor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./gemma4processor/prepare%28input%29.md)
- [func preprocess(image: CIImage, processing: UserInput.Processing?) throws -> (MLXArray, THW)](./gemma4processor/preprocess%28image,processing%29.md)
- [func processVideos([UserInput.Video], processing: UserInput.Processing?) async throws -> (pixels: MLXArray, frameCounts: [Int])](./gemma4processor/processvideos%28_,processing%29.md)
  Sample and preprocess the frames of each video into a single `[totalFrames, C, H, W]` pixel tensor (frames from all videos concatenated), plus the per-video frame count used to expand the `<video>` placeholders. Frames are resized to `config.videoFixedSize` so the vision tower’s leading pooled tokens fit the per-frame video budget.

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processor)*