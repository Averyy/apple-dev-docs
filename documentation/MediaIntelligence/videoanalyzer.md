# VideoAnalyzer

**Framework**: Media Intelligence  
**Kind**: class

An object that analyzes video assets for highlights and key frames.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class VideoAnalyzer
```

## Mentions

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)

#### Overview

A video analyzer is the central object in the video analysis pipeline. Access it through the static [`shared`](videoanalyzer/shared.md) property and pass it a [`MediaIntelligenceVideoAsset`](mediaintelligencevideoasset.md) along with one or more request objects. The analyzer processes the video and returns a tuple containing one [`Result`](https://developer.apple.com/documentation/swift/result) per request, in the same order you provide them.

## Topics

### Analyzing a video asset
- [static let shared: VideoAnalyzer](videoanalyzer/shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Request](videoanalyzer/request.md)
  A type that describes a video analysis operation.
- [VideoAnalyzer.Result](videoanalyzer/result.md)
  A type that represents the output of a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](videoanalyzer/analyze(_:for:).md)
  Analyzes a video asset using the specified requests.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)
  Identify keyframes and highlight segments using on-device analysis.
- [struct MediaIntelligenceVideoAsset](mediaintelligencevideoasset.md)
  A video asset to analyze.
- [class HighlightAnalysisRequest](highlightanalysisrequest.md)
  A request that identifies the most engaging segments of a video.
- [class KeyFrameAnalysisRequest](keyframeanalysisrequest.md)
  A request that identifies the best representative frame of a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer)*