---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:targetfps:maxframes:frameprocessing:)"
framework: "mlx-swift-lm/MLXVLM"
---

# asProcessedSequence(_:targetFPS:maxFrames:frameProcessing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

Extract and process a sequence of video frames using a dynamic target FPS function.

## Declaration

```swift
static func asProcessedSequence(_ video: UserInput.Video, targetFPS: (CMTime) -> Double, maxFrames: Int = Int.max, frameProcessing: (VideoFrame) throws -> VideoFrame = { $0 }) async throws -> ProcessedFrames
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:targetfps:maxframes:frameprocessing:))*