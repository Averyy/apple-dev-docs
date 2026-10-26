---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:samplespersecond:frameprocessing:)-6y2hy"
framework: "mlx-swift-lm/MLXVLM"
---

# asProcessedSequence(_:samplesPerSecond:frameProcessing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

Extract and process a sequence of video frames at a constant sample rate.

## Declaration

```swift
static func asProcessedSequence(_ video: UserInput.Video, samplesPerSecond: Int, frameProcessing: (VideoFrame) throws -> VideoFrame = { $0 }) async throws -> ProcessedFrames
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:samplespersecond:frameprocessing:)-6y2hy)*