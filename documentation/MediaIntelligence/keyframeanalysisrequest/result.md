# KeyFrameAnalysisRequest.Result

**Framework**: Media Intelligence  
**Kind**: struct

The output of a key frame analysis.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Result
```

#### Overview

[`KeyFrameAnalysisRequest.Result`](keyframeanalysisrequest/result.md) contains the timestamp of the frame the framework selects as the best representative of the video. Use this [`CMTime`](https://developer.apple.com/documentation/coremedia/cmtime) value to seek a player to that position or to extract a thumbnail.

## Topics

### Inspecting the result
- [let timestamp: CMTime](keyframeanalysisrequest/result/timestamp.md)
  The timestamp of the key frame.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VideoAnalyzer.Result](videoanalyzer/result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/keyframeanalysisrequest/result)*