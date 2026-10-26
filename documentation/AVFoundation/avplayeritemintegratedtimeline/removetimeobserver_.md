# removeTimeObserver:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels a previously registered time observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
- (void) removeTimeObserver:(id<AVPlayerItemIntegratedTimelineObserver>) observer;
```

## See Also

### Observing time changes
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](./addperiodictimeobserverforinterval_queue_usingblock_.md)
  Requests invocation of a block during playback to report changing time.
- [- addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:](./addboundarytimeobserverforsegment_offsetsintosegment_queue_usingblock_.md)
  Requests invocation of a block when traversing an offset in a segment during playback.
- [protocol AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md)
  A protocol for objects that perform timeline observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/removetimeobserver:)*