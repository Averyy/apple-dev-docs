# AVPlayerItemIntegratedTimeline.PeriodicTimes

**Framework**: AVFoundation  
**Kind**: struct

An asynchronous sequence of periodic time values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct PeriodicTimes
```

## Topics

### Iterating Elements
- [AVPlayerItemIntegratedTimeline.PeriodicTimes.Iterator](avplayeritemintegratedtimeline/periodictimes/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func periodicTimes(forInterval: CMTime) -> AVPlayerItemIntegratedTimeline.PeriodicTimes](avplayeritemintegratedtimeline/periodictimes(forinterval:).md)
  Returns an asynchronous sequence of times periodically as playback progresses.
- [func boundaryTimes(for: AVPlayerItemSegment, offsetsIntoSegment: [CMTime]) -> AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes(for:offsetsintosegment:).md)
  Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes.md)
  An asynchronous sequence of boundary time values.
- [protocol AVPlayerItemIntegratedTimelineObserver](avplayeritemintegratedtimelineobserver.md)
  A protocol for objects that perform timeline observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/periodictimes)*