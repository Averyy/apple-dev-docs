# HighlightAnalysisRequest

**Framework**: Media Intelligence  
**Kind**: class

A request that identifies the most engaging segments of a video.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class HighlightAnalysisRequest
```

## Mentions

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)

#### Overview

[`HighlightAnalysisRequest`](highlightanalysisrequest.md) asks [`VideoAnalyzer`](videoanalyzer.md) to find the highlight segments of a video and score every segment for engagement. Pass it to [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) to receive a [`HighlightAnalysisRequest.Result`](highlightanalysisrequest/result.md) value.

## Topics

### Creating a request
- [init()](highlightanalysisrequest/init.md)
  Creates a highlight analysis request.
### Inspecting the result
- [HighlightAnalysisRequest.Result](highlightanalysisrequest/result.md)
  The output of a highlight analysis.

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
- [class KeyFrameAnalysisRequest](keyframeanalysisrequest.md)
  A request that identifies the best representative frame of a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/highlightanalysisrequest)*