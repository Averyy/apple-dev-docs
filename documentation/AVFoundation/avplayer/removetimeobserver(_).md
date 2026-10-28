# removeTimeObserver(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels a previously registered periodic or boundary time observer.

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
func removeTimeObserver(_ observer: Any)
```

```objc
- (void) removeTimeObserver:(id) observer;
```

## Mentions

- [Monitoring playback progress in your app](../monitoring-playback-progress-in-your-app.md)

## Discussion

Upon return, the caller is guaranteed that no new time observer blocks will begin executing. Depending on the calling thread and the queue used to add the time observer, an in-flight block may continue to execute after this method returns. You can guarantee synchronous time observer removal by enqueuing the call to `removeTimeObserver` on that queue. Alternatively, call `dispatch_sync(queue, ^{})` after `removeTimeObserver` to wait for any in-flight blocks to finish executing.

You should use this method to explicitly cancel each time observer added using [`addPeriodicTimeObserver(forInterval:queue:using:)`](./addperiodictimeobserver%28forinterval,queue,using%29.md) and [`addBoundaryTimeObserver(forTimes:queue:using:)`](./addboundarytimeobserver%28fortimes,queue,using%29.md).

The following shows a common implementation to remove a registered time observer:

**Swift**:

```swift
func removePeriodicTimeObserver() {
    // If a time observer exists, remove it
    if let token = timeObserverToken {
        player.removeTimeObserver(token)
        timeObserverToken = nil
    }
}
```

**Objective-C**:

```objc
- (void)removeBoundaryTimeObserver {
    if (self.timeObserverToken) {
        [self.player removeTimeObserver:self.timeObserverToken];
        self.timeObserverToken = nil;
    }
}
```

## Parameters

- `observer`: An object returned by a previous call to [`addPeriodicTimeObserver(forInterval:queue:using:)`](./addperiodictimeobserver%28forinterval,queue,using%29.md) or [`addBoundaryTimeObserver(forTimes:queue:using:)`](./addboundarytimeobserver%28fortimes,queue,using%29.md).

## See Also

### Observing playback time
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the current player item.
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](./addperiodictimeobserver%28forinterval,queue,using%29.md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](./addboundarytimeobserver%28fortimes,queue,using%29.md)
  Requests the invocation of a block when specified times are traversed during normal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/removetimeobserver(_:))*