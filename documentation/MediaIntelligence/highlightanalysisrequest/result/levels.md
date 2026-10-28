# levels

**Framework**: Media Intelligence  
**Kind**: property  
**Role**: Instance Property

The engagement level of each segment in the video.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let levels: [(timeRange: CMTimeRange, level: Float)]
```

## Mentions

- [Finding the best moments in a video](../../finding-the-best-moments-in-a-video.md)

## Discussion

Each element pairs a [`CMTimeRange`](../../../CoreMedia/cmtimerange.md) with a floating-point level value from `0` (least engaging) to `9` (most engaging). The array covers every segment in the video, not just the highlights.

## See Also

### Inspecting the result
- [let highlights: [CMTimeRange]](./highlights.md)
  The time ranges the framework identifies as highlights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/highlightanalysisrequest/result/levels)*