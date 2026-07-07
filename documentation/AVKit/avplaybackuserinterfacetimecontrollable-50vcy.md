# AVPlaybackUserInterfaceTimeControllable

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
protocol AVPlaybackUserInterfaceTimeControllable : AnyObject, Observable
```

## Topics

### Instance Properties
- [var currentSegment: AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimecontrollable-50vcy/currentsegment.md)
  The segment containing the current playback position.
- [var playbackPosition: AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfacetimecontrollable-50vcy/playbackposition.md)
  A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be observable.
- [var seekableTimeRanges: [CMTimeRange]?](avplaybackuserinterfacetimecontrollable-50vcy/seekabletimeranges.md)
  Time ranges within the timeline where seeking operations are permitted.
- [var segments: [AVPlaybackUserInterfaceTimelineSegment]](avplaybackuserinterfacetimecontrollable-50vcy/segments.md)
  Segments representing different content types within the timeline.
- [var timeRange: CMTimeRange](avplaybackuserinterfacetimecontrollable-50vcy/timerange.md)
  The time range representing the total duration and bounds of the media content.
### Instance Methods
- [func seek(to: CMTime, tolerance: CMTime)](avplaybackuserinterfacetimecontrollable-50vcy/seek(to:tolerance:).md)
  Requests a seek to the specified position.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy)*