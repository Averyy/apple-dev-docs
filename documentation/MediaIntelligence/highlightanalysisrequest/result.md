# HighlightAnalysisRequest.Result

**Framework**: Media Intelligence  
**Kind**: struct

The output of a highlight analysis.

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

This type describes the highlights and engagement levels the framework finds in a video.

[`highlights`](highlightanalysisrequest/result/highlights.md) lists the time ranges the framework identifies as highlights. Use these ranges to build a highlight reel or to seek directly to the most interesting moments.

[`levels`](highlightanalysisrequest/result/levels.md) provides a finer-grained view where every segment in the video gets a floating-point engagement level from `0` (least engaging) to `9` (most engaging). Use these values to visualize a video’s pacing or to let people scrub through segments by interest level.

## Topics

### Inspecting the result
- [let highlights: [CMTimeRange]](highlightanalysisrequest/result/highlights.md)
  The time ranges the framework identifies as highlights.
- [let levels: [(timeRange: CMTimeRange, level: Float)]](highlightanalysisrequest/result/levels.md)
  The engagement level of each segment in the video.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VideoAnalyzer.Result](videoanalyzer/result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/highlightanalysisrequest/result)*