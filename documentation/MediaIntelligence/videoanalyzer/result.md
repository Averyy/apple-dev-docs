# VideoAnalyzer.Result

**Framework**: Media Intelligence  
**Kind**: protocol  
**Role**: Protocol

A type that represents the output of a video analysis operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol Result : Sendable
```

## Overview

This type is the base protocol for analysis result types. You receive a typed value conforming to this protocol when [`analyze(_:for:)`](./analyze%28_,for%29.md) succeeds for a particular request. The framework uses the request’s associated [`Result`](./request/result.md) type to determine the concrete type returned for each element in the tuple.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [HighlightAnalysisRequest.Result](../highlightanalysisrequest/result.md)
- [KeyFrameAnalysisRequest.Result](../keyframeanalysisrequest/result.md)

## See Also

### Analyzing a video asset
- [static let shared: VideoAnalyzer](./shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Request](./request.md)
  A type that describes a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](./analyze%28_,for%29.md)
  Analyzes a video asset using the specified requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/result)*