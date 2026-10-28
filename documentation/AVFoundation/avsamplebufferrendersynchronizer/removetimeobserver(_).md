# removeTimeObserver(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels the specified time observer.

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
func removeTimeObserver(_ observer: Any)
```

```objc
- (void) removeTimeObserver:(id) observer;
```

## Discussion

Use this method to explicitly cancel time observers added using [`addPeriodicTimeObserver(forInterval:queue:using:)`](./addperiodictimeobserver%28forinterval,queue,using%29.md) or [`addBoundaryTimeObserver(forTimes:queue:using:)`](./addboundarytimeobserver%28fortimes,queue,using%29.md)

Upon return, the caller is guaranteed that no new time observer blocks will begin executing. Depending on the calling thread and the queue used to add the time observer, an in-flight block may continue to execute after this method returns. You can guarantee synchronous time observer removal by enqueuing the call to `removeTimeObserver:` on that queue. Call [`sync(execute:)`](../../Dispatch/dispatchqueue/sync%28execute%29-3segw.md) after `removeTimeObserver:` to wait for any in-flight blocks to finish executing.

## Parameters

- `observer`: The time observer to be cancelled.

## See Also

### Observing time
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](./addperiodictimeobserver%28forinterval,queue,using%29.md)
  Requests invocation of a block during rendering at specified time intervals.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](./addboundarytimeobserver%28fortimes,queue,using%29.md)
  Requests invocation of a block when specified times are traversed during normal rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removetimeobserver(_:))*