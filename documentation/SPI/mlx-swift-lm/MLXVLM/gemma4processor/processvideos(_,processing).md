---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processor/processvideos(_:processing:)"
framework: "mlx-swift-lm/MLXVLM"
---

# processVideos(_:processing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Sample and preprocess the frames of each video into a single `[totalFrames, C, H, W]` pixel tensor (frames from all videos concatenated), plus the per-video frame count used to expand the `<video>` placeholders. Frames are resized to `config.videoFixedSize` so the vision tower’s leading pooled tokens fit the per-frame video budget.

## Declaration

```swift
func processVideos(_ videos: [UserInput.Video], processing: UserInput.Processing?) async throws -> (pixels: MLXArray, frameCounts: [Int])
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processor/processvideos(_:processing:))*