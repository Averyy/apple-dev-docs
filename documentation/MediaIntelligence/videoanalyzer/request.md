# VideoAnalyzer.Request

**Framework**: Media Intelligence  
**Kind**: protocol

A type that describes a video analysis operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol Request : Sendable
```

#### Overview

The framework provides two built-in request types: [`HighlightAnalysisRequest`](highlightanalysisrequest.md) and [`KeyFrameAnalysisRequest`](keyframeanalysisrequest.md).

## Topics

### Associated Types
- [associatedtype Result : VideoAnalyzer.Result](videoanalyzer/request/result.md)

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [HighlightAnalysisRequest](highlightanalysisrequest.md)
- [KeyFrameAnalysisRequest](keyframeanalysisrequest.md)

## See Also

- [static let shared: VideoAnalyzer](videoanalyzer/shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Result](videoanalyzer/result.md)
  A type that represents the output of a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](videoanalyzer/analyze(_:for:).md)
  Analyzes a video asset using the specified requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/request)*