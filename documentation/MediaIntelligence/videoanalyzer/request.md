# VideoAnalyzer.Request

**Framework**: Media Intelligence  
**Kind**: protocol  
**Role**: Protocol

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

## Overview

The framework provides two built-in request types: [`HighlightAnalysisRequest`](../highlightanalysisrequest.md) and [`KeyFrameAnalysisRequest`](../keyframeanalysisrequest.md).

## Topics

### Associated Types
- [associatedtype Result : VideoAnalyzer.Result](./request/result.md)

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [HighlightAnalysisRequest](../highlightanalysisrequest.md)
- [KeyFrameAnalysisRequest](../keyframeanalysisrequest.md)

## See Also

### Analyzing a video asset
- [static let shared: VideoAnalyzer](./shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Result](./result.md)
  A type that represents the output of a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](./analyze%28_,for%29.md)
  Analyzes a video asset using the specified requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/request)*