---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:userprocessing:targetfps:maxframes:frameprocessing:)"
framework: "mlx-swift-lm/MLXVLM"
---

# asProcessedSequence(_:userProcessing:targetFPS:maxFrames:frameProcessing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

Extract and process a sequence of video frames according to `UserInput.Processing` options.

## Declaration

```swift
static func asProcessedSequence(_ video: UserInput.Video, userProcessing: UserInput.Processing, targetFPS: ((CMTime) -> Double)? = nil, maxFrames: Int = Int.max, frameProcessing: (VideoFrame) throws -> VideoFrame = { $0 }) async throws -> ProcessedFrames
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:userprocessing:targetfps:maxframes:frameprocessing:))*