# KeyFrameAnalysisRequest

**Framework**: Media Intelligence  
**Kind**: class

A request that identifies the best representative frame of a video.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class KeyFrameAnalysisRequest
```

## Mentions

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)

#### Overview

Use this type to find the single frame that best represents the overall content of the video. Pass it to [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) to receive a [`KeyFrameAnalysisRequest.Result`](keyframeanalysisrequest/result.md) value containing the frame’s timestamp.

Use the timestamp to seek a player to that position or to extract a thumbnail image.

## Topics

### Creating a request
- [init()](keyframeanalysisrequest/init.md)
  Creates a key frame analysis request.
### Inspecting the result
- [KeyFrameAnalysisRequest.Result](keyframeanalysisrequest/result.md)
  The output of a key frame analysis.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VideoAnalyzer.Request](videoanalyzer/request.md)

## See Also

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)
  Identify keyframes and highlight segments using on-device analysis.
- [class VideoAnalyzer](videoanalyzer.md)
  An object that analyzes video assets for highlights and key frames.
- [struct MediaIntelligenceVideoAsset](mediaintelligencevideoasset.md)
  A video asset to analyze.
- [class HighlightAnalysisRequest](highlightanalysisrequest.md)
  A request that identifies the most engaging segments of a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/keyframeanalysisrequest)*