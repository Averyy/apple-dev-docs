# currentPlaybackPosition

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

The current playback position within the media time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var currentPlaybackPosition: CMTime { get set }
```

## See Also

- [var timeRange: CMTimeRange](avinterfacetimecontrollable-63tkp/timerange.md)
  The time range representing the total duration and bounds of the media content.
- [var currentSegment: AVInterfaceTimelineSegment](avinterfacetimecontrollable-63tkp/currentsegment.md)
  The segment containing the current playback position.
- [var seekableTimeRanges: [CMTimeRange]?](avinterfacetimecontrollable-63tkp/seekabletimeranges.md)
  Time ranges within the timeline where seeking operations are permitted.
- [var segments: [AVInterfaceTimelineSegment]](avinterfacetimecontrollable-63tkp/segments.md)
  Segments representing different content types within the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable-63tkp/currentplaybackposition)*