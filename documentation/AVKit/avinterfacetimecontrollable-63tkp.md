# AVInterfaceTimeControllable

**Framework**: AVKit  
**Kind**: protocol

Provides time control and navigation capabilities for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVInterfaceTimeControllable : Observable
```

## Topics

### Inspecting the timeline
- [var timeRange: CMTimeRange](avinterfacetimecontrollable-63tkp/timerange.md)
  The time range representing the total duration and bounds of the media content.
- [var currentPlaybackPosition: CMTime](avinterfacetimecontrollable-63tkp/currentplaybackposition.md)
  The current playback position within the media time.
- [var currentSegment: AVInterfaceTimelineSegment](avinterfacetimecontrollable-63tkp/currentsegment.md)
  The segment containing the current playback position.
- [var seekableTimeRanges: [CMTimeRange]?](avinterfacetimecontrollable-63tkp/seekabletimeranges.md)
  Time ranges within the timeline where seeking operations are permitted.
- [var segments: [AVInterfaceTimelineSegment]](avinterfacetimecontrollable-63tkp/segments.md)
  Segments representing different content types within the timeline.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)

## See Also

- [class AVInterfaceTimelineSegment](avinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable-63tkp)*