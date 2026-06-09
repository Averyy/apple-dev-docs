# levels

**Framework**: Media Intelligence  
**Kind**: property

The engagement level of each segment in the video.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let levels: [(timeRange: CMTimeRange, level: Float)]
```

## Mentions

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)

#### Discussion

Each element pairs a [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) with a floating-point level value from `0` (least engaging) to `9` (most engaging). The array covers every segment in the video, not just the highlights.

## See Also

- [let highlights: [CMTimeRange]](highlightanalysisrequest/result/highlights.md)
  The time ranges the framework identifies as highlights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/highlightanalysisrequest/result/levels)*