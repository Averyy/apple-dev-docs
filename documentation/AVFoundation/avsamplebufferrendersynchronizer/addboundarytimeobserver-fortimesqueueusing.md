# addBoundaryTimeObserver(forTimes:queue:using:)

**Framework**: AVFoundation  
**Kind**: method

Requests invocation of a block when specified times are traversed during normal rendering.

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
func addBoundaryTimeObserver(forTimes times: [NSValue], queue: dispatch_queue_t?, using block: @escaping () -> Void) -> Any
```

#### Return Value

An object that conforms to [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class). You must retain this value as long as you want the time observer to be invoked by the synchronizer. Pass this object to [`removeTimeObserver(_:)`](avsamplebufferrendersynchronizer/removetimeobserver(_:).md) to cancel time observation.

#### Discussion

Always pair a call to this method with a call to [`removeTimeObserver(_:)`](avsamplebufferrendersynchronizer/removetimeobserver(_:).md). Releasing the observer without calling `removeTimeObserver(_:)` results in undefined behavior.

## Parameters

- `times`: An array containing the times for which the observer requests notification.
- `queue`: The serial queue the block should be unqueued on. If you pass  , the main queue is used. Passing a concurrent queue results in undefined behavior.
- `block`: The block to be invoked when any of the specified times is crossed during normal rendering.

## See Also

- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests invocation of a block during rendering at specified time intervals.
- [func removeTimeObserver(Any)](avsamplebufferrendersynchronizer/removetimeobserver(_:).md)
  Cancels the specified time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes:queue:using:))*