# currentTime()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the current time of the current player item.

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
nonisolated
func currentTime() -> CMTime
```

```objc
- (CMTime) currentTime;
```

## Return Value

The current time of the current player item.

## Discussion

This property isn’t key-value observable. To observe the player’s time, use [`addPeriodicTimeObserver(forInterval:queue:using:)`](./addperiodictimeobserver%28forinterval,queue,using%29.md) or [`addBoundaryTimeObserver(forTimes:queue:using:)`](./addboundarytimeobserver%28fortimes,queue,using%29.md).

## See Also

### Observing playback time
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](./addperiodictimeobserver%28forinterval,queue,using%29.md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](./addboundarytimeobserver%28fortimes,queue,using%29.md)
  Requests the invocation of a block when specified times are traversed during normal playback.
- [func removeTimeObserver(Any)](./removetimeobserver%28_%29.md)
  Cancels a previously registered periodic or boundary time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/currenttime())*