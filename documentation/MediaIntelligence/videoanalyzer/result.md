# VideoAnalyzer.Result

**Framework**: Media Intelligence  
**Kind**: protocol

A type that represents the output of a video analysis operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Result : Sendable
```

#### Overview

This type is the base protocol for analysis result types. You receive a typed value conforming to this protocol when [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md) succeeds for a particular request. The framework uses the request’s associated [`Result`](videoanalyzer/request/result.md) type to determine the concrete type returned for each element in the tuple.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [HighlightAnalysisRequest.Result](highlightanalysisrequest/result.md)
- [KeyFrameAnalysisRequest.Result](keyframeanalysisrequest/result.md)

## See Also

- [static let shared: VideoAnalyzer](videoanalyzer/shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Request](videoanalyzer/request.md)
  A type that describes a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](videoanalyzer/analyze(_:for:).md)
  Analyzes a video asset using the specified requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/result)*