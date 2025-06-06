# AVPlayerItemIntegratedTimelineObserver

**Framework**: AVFoundation  
**Kind**: protocol

A protocol for objects that perform timeline observations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVPlayerItemIntegratedTimelineObserver : NSObjectProtocol
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func periodicTimes(forInterval: CMTime) -> AVPlayerItemIntegratedTimeline.PeriodicTimes](avplayeritemintegratedtimeline/periodictimes(forinterval:).md)
  Returns an asynchronous sequence of times periodically as playback progresses.
- [func boundaryTimes(for: AVPlayerItemSegment, offsetsIntoSegment: [CMTime]) -> AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes(for:offsetsintosegment:).md)
  Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes.md)
  An asynchronous sequence of boundary time values.
- [AVPlayerItemIntegratedTimeline.PeriodicTimes](avplayeritemintegratedtimeline/periodictimes.md)
  An asynchronous sequence of periodic time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelineobserver)*