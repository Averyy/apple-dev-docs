# addPeriodicTimeObserver(forInterval:queue:using:)

**Framework**: AVFoundation  
**Kind**: method

Requests invocation of a block during rendering at specified time intervals.

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
func addPeriodicTimeObserver(forInterval interval: CMTime, queue: dispatch_queue_t?, using block: @escaping (CMTime) -> Void) -> Any
```

#### Return Value

An object that conforms to [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class). You must retain this value as long as you want the time observer to be invoked by the synchronizer. Pass this object to [`removeTimeObserver(_:)`](avsamplebufferrendersynchronizer/removetimeobserver(_:).md) to cancel time observation.

#### Discussion

The block associated with this method is invoked at the specified time intervals, interpreted according to the timeline of the timebase. The block is also invoked whenever there is a time jump or rendering starts or stops.

If a very short time interval is used, the synchronizer may invoke the block less frequently than requested. However, the synchronizer will invoke the block often enough for the client to update indications of the current time appropriately in its end-user interface.

Always pair a call to this method with a call to [`removeTimeObserver(_:)`](avsamplebufferrendersynchronizer/removetimeobserver(_:).md). Releasing the observer without calling `removeTimeObserver(_:)` results in undefined behavior.

## Parameters

- `interval`: The specified time interval requesting block invocation during rendering.
- `queue`: The serial queue the block should be unqueued on. If you pass  , the main queue is used. Passing a concurrent queue results in undefined behavior.
- `block`: The block to be invoked periodically.

## See Also

- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests invocation of a block when specified times are traversed during normal rendering.
- [func removeTimeObserver(Any)](avsamplebufferrendersynchronizer/removetimeobserver(_:).md)
  Cancels the specified time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval:queue:using:))*