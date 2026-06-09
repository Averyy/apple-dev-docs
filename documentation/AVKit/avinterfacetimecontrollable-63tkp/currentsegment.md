# currentSegment

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

The segment containing the current playback position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var currentSegment: AVInterfaceTimelineSegment { get }
```

## See Also

- [var timeRange: CMTimeRange](avinterfacetimecontrollable-63tkp/timerange.md)
  The time range representing the total duration and bounds of the media content.
- [var currentPlaybackPosition: CMTime](avinterfacetimecontrollable-63tkp/currentplaybackposition.md)
  The current playback position within the media time.
- [var seekableTimeRanges: [CMTimeRange]?](avinterfacetimecontrollable-63tkp/seekabletimeranges.md)
  Time ranges within the timeline where seeking operations are permitted.
- [var segments: [AVInterfaceTimelineSegment]](avinterfacetimecontrollable-63tkp/segments.md)
  Segments representing different content types within the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable-63tkp/currentsegment)*