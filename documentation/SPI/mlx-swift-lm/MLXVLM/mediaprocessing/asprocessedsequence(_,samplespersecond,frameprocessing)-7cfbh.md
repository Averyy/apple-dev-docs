---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:samplespersecond:frameprocessing:)-7cfbh"
framework: "mlx-swift-lm/MLXVLM"
---

# asProcessedSequence(_:samplesPerSecond:frameProcessing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

> **Deprecated**: Use MediaProcessing.asProcessedSequence() with the Video directly

## Declaration

```swift
static func asProcessedSequence(_ asset: AVAsset, samplesPerSecond: Int, frameProcessing: (VideoFrame) throws -> VideoFrame = { $0 }) async throws -> ProcessedFrames
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:samplespersecond:frameprocessing:)-7cfbh)*