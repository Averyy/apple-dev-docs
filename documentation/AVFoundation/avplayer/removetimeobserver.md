# removeTimeObserver(_:)

**Framework**: AVFoundation  
**Kind**: method

Cancels a previously registered periodic or boundary time observer.

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
nonisolated
func removeTimeObserver(_ observer: Any)
```

## Mentions

- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md)

#### Discussion

Upon return, the caller is guaranteed that no new time observer blocks will begin executing. Depending on the calling thread and the queue used to add the time observer, an in-flight block may continue to execute after this method returns. You can guarantee synchronous time observer removal by enqueuing the call to `removeTimeObserver` on that queue. Alternatively, call `dispatch_sync(queue, ^{})` after `removeTimeObserver` to wait for any in-flight blocks to finish executing.

You should use this method to explicitly cancel each time observer added using [`addPeriodicTimeObserver(forInterval:queue:using:)`](avplayer/addperiodictimeobserver(forinterval:queue:using:).md) and [`addBoundaryTimeObserver(forTimes:queue:using:)`](avplayer/addboundarytimeobserver(fortimes:queue:using:).md).

The following shows a common implementation to remove a registered time observer:

## Parameters

- `observer`: An object returned by a previous call to   or  .

## See Also

- [func currentTime() -> CMTime](avplayer/currenttime.md)
  Returns the current time of the current player item.
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avplayer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avplayer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests the invocation of a block when specified times are traversed during normal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/removetimeobserver(_:))*