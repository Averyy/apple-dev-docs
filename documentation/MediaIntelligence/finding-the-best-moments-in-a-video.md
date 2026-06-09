# Finding the best moments in a video

**Framework**: Media Intelligence

Identify keyframes and highlight segments using on-device analysis.

#### Overview

People often want to find the best moments in a video, whether to jump to the most exciting parts of a long recording or to choose a thumbnail that represents the content rather than a generic first frame. The [`VideoAnalyzer`](videoanalyzer.md) class provides on-device analysis that evaluates engagement across a video and identifies its highlights and most representative frame.

You access the analyzer through its [`shared`](videoanalyzer/shared.md) property and pass it a [`MediaIntelligenceVideoAsset`](mediaintelligencevideoasset.md) along with one or more request objects that describe the analysis you want. The analyzer processes the video and returns a typed result for each request.

Because video analysis is computationally intensive, the framework queues concurrent requests and processes them serially. If multiple tasks call [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) at the same time, each request waits for the previous one to finish. The framework doesn’t impose a maximum queue depth or timeout, so your app is responsible for managing how many analyses it enqueues.

#### Prepare a Video Asset

Create a [`MediaIntelligenceVideoAsset`](mediaintelligencevideoasset.md) that identifies the video you want to analyze. Each asset takes a unique identifier you assign and a [`MediaIntelligenceVideoAsset.Kind`](mediaintelligencevideoasset/kind-swift.enum.md) value that tells the framework how to access the video data. Pass [`MediaIntelligenceVideoAsset.Kind.url(_:)`](mediaintelligencevideoasset/kind-swift.enum/url(_:).md) with a file URL pointing to the video on disk:

```swift
let asset = MediaIntelligenceVideoAsset(
    id: MediaIntelligenceVideoAsset.ID(videoURL.lastPathComponent),
    kind: .url(videoURL)
)
```

This example uses the URL’s last path component as the identifier, but you can use any string that uniquely identifies the video in your app.

#### Find the Keyframe

The simplest analysis you can perform is finding the *keyframe*, which is a single frame that best represents the video’s content. Create a [`KeyFrameAnalysisRequest`](keyframeanalysisrequest.md) and pass it to [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md):

```swift
let request = KeyFrameAnalysisRequest()
let result = try await VideoAnalyzer.shared.analyze(asset, for: request)

switch result {
case .success(let keyframe):
    // Move the player to this frame or extract a thumbnail.
    let timestamp = keyframe.timestamp
case .failure(let error):
    // Handle the error.
}
```

The keyframe’s `timestamp` is a [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) value that identifies the most representative frame in the video. Use it to move the player to that frame or generate a thumbnail image.

> **Note**: A convenient way to generate a thumbnail from the keyframe timestamp is with [`AVAssetImageGenerator`](https://developer.apple.com/documentation/AVFoundation/AVAssetImageGenerator). For more information, see [`Creating images from a video asset`](https://developer.apple.com/documentation/AVFoundation/creating-images-from-a-video-asset).

#### Find Video Highlights

To understand engagement across an entire video rather than a single representative frame, create a [`HighlightAnalysisRequest`](highlightanalysisrequest.md). The result provides two complementary perspectives on engagement:

- **[`highlights`](highlightanalysisrequest/result/highlights.md)**: An array of [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) values identifying the most engaging segments. Use these to build a highlight reel or seek directly to interesting moments.
- **[`levels`](highlightanalysisrequest/result/levels.md)**: A segment-by-segment breakdown where every portion of the video receives a floating-point engagement level from `0` (least engaging) to `9` (most engaging). Use levels to visualize pacing or let people scrub by interest.

The following example analyzes a video for highlights and iterates through both the highlight ranges and per-segment engagement levels:

```swift
let result = try await VideoAnalyzer.shared.analyze(asset, for: HighlightAnalysisRequest())

switch result {
case .success(let analysis):
    for highlight in analysis.highlights {
        // Each highlight is a time range that identifies an engaging segment.
    }
    for segment in analysis.levels {
        // Each segment pairs a time range with a floating-point engagement level.
    }
case .failure(let error):
    // Handle the error.
}
```

#### Combine Multiple Requests

When you need highlights and a keyframe from a video, pass both requests to a single [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) call. The analyzer decodes the video once regardless of how many requests you pass, making the combined call more efficient. Because each request produces its own [`Result`](https://developer.apple.com/documentation/Swift/Result) value, you can handle successes and failures independently. The following example requests both analyses:

```swift
let (highlightResult, keyframeResult) = try await VideoAnalyzer.shared.analyze(
    asset,
    for: HighlightAnalysisRequest(),
         KeyFrameAnalysisRequest()
)

switch highlightResult {
case .success(let analysis):
    // Work with highlights and engagement levels.
case .failure(let error):
    // Handle the highlight analysis error.
}

switch keyframeResult {
case .success(let keyframe):
    // Use the keyframe timestamp.
case .failure(let error):
    // Handle the keyframe analysis error.
}
```

#### Cancel an in Progress Analysis

The [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) method supports cooperative cancellation through Swift concurrency. When you cancel the task that called [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md), the analyzer checks for cancellation periodically during processing and returns early. Because the analyzer needs to cancel in-progress work on the Neural Engine, the method can take a moment to return.

The following example wraps an analysis call in a task and cancels it in response to a person navigating away:

```swift
let analysisTask = Task {
    let result = try await VideoAnalyzer.shared.analyze(asset, for: HighlightAnalysisRequest())
    // Process the result.
}

// Cancel the analysis when the person navigates away.
analysisTask.cancel()
```

## See Also

- [class VideoAnalyzer](videoanalyzer.md)
  An object that analyzes video assets for highlights and key frames.
- [struct MediaIntelligenceVideoAsset](mediaintelligencevideoasset.md)
  A video asset to analyze.
- [class HighlightAnalysisRequest](highlightanalysisrequest.md)
  A request that identifies the most engaging segments of a video.
- [class KeyFrameAnalysisRequest](keyframeanalysisrequest.md)
  A request that identifies the best representative frame of a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/finding-the-best-moments-in-a-video)*