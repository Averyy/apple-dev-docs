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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelineobserver)*