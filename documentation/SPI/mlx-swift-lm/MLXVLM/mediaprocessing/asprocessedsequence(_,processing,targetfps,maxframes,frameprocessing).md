---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:processing:targetfps:maxframes:frameprocessing:)"
framework: "mlx-swift-lm/MLXVLM"
---

# asProcessedSequence(_:processing:targetFPS:maxFrames:frameProcessing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Type Method

Extract and process a sequence of video frames according to video processing configuration.

## Declaration

```swift
static func asProcessedSequence(_ video: UserInput.Video, processing: UserInput.VideoProcessing = .init(), targetFPS: ((CMTime) -> Double)? = nil, maxFrames: Int = Int.max, frameProcessing: (VideoFrame) throws -> VideoFrame = { $0 }) async throws -> ProcessedFrames
```

#### Return Value

`ProcessedFrames` containing extracted MLXArray frames, timestamps, and total duration.

## Parameters

- `video`: The video to extract frames from (`AVAsset`, `URL`, or decoded `VideoFrame`s).
- `processing`: Video processing configuration (such as `targetFrames` or `targetFramesPerSecond`).
- `targetFPS`: Optional closure computing target FPS given duration; used when `processing` has neither `targetFrames` nor `targetFramesPerSecond`.
- `maxFrames`: Maximum frame count budget.
- `frameProcessing`: Transformation applied to each individual video frame.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing/asprocessedsequence(_:processing:targetfps:maxframes:frameprocessing:))*