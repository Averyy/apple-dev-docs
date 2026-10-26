# addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Requests invocation of a block when traversing an offset in a segment during playback.

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
- (id<AVPlayerItemIntegratedTimelineObserver>) addBoundaryTimeObserverForSegment:(AVPlayerItemSegment *) segment offsetsIntoSegment:(NSArray *) offsetsIntoSegment queue:(dispatch_queue_t) queue usingBlock:(void (^)(BOOL success)) block;
```

## See Also

### Observing time changes
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](./addperiodictimeobserverforinterval_queue_usingblock_.md)
  Requests invocation of a block during playback to report changing time.
- [- removeTimeObserver:](./removetimeobserver_.md)
  Cancels a previously registered time observer.
- [protocol AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md)
  A protocol for objects that perform timeline observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/addboundarytimeobserverforsegment:offsetsintosegment:queue:usingblock:)*