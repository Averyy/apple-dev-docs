# AVPlayerItemIntegratedTimelineObserver

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A protocol for objects that perform timeline observations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol AVPlayerItemIntegratedTimelineObserver : NSObjectProtocol
```

```objc
@protocol AVPlayerItemIntegratedTimelineObserver <NSObject>
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing time changes
- [func periodicTimes(forInterval: CMTime) -> AVPlayerItemIntegratedTimeline.PeriodicTimes](./avplayeritemintegratedtimeline/periodictimes%28forinterval%29.md)
  Returns an asynchronous sequence of times periodically as playback progresses.
- [func boundaryTimes(for: AVPlayerItemSegment, offsetsIntoSegment: [CMTime]) -> AVPlayerItemIntegratedTimeline.BoundaryTimes](./avplayeritemintegratedtimeline/boundarytimes%28for,offsetsintosegment%29.md)
  Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [AVPlayerItemIntegratedTimeline.BoundaryTimes](./avplayeritemintegratedtimeline/boundarytimes.md)
  An asynchronous sequence of boundary time values.
- [AVPlayerItemIntegratedTimeline.PeriodicTimes](./avplayeritemintegratedtimeline/periodictimes.md)
  An asynchronous sequence of periodic time values.
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](./avplayeritemintegratedtimeline/addperiodictimeobserverforinterval_queue_usingblock_.md)
  Requests invocation of a block during playback to report changing time.
- [- addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:](./avplayeritemintegratedtimeline/addboundarytimeobserverforsegment_offsetsintosegment_queue_usingblock_.md)
  Requests invocation of a block when traversing an offset in a segment during playback.
- [- removeTimeObserver:](./avplayeritemintegratedtimeline/removetimeobserver_.md)
  Cancels a previously registered time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelineobserver)*