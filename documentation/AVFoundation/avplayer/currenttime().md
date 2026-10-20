# currentTime()

**Framework**: AVFoundation  
**Kind**: method

Returns the current time of the current player item.

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
func currentTime() -> CMTime
```

#### Return Value

The current time of the current player item.

#### Discussion

This property isn’t key-value observable. To observe the player’s time, use [`addPeriodicTimeObserver(forInterval:queue:using:)`](avplayer/addperiodictimeobserver(forinterval:queue:using:).md) or [`addBoundaryTimeObserver(forTimes:queue:using:)`](avplayer/addboundarytimeobserver(fortimes:queue:using:).md).

## See Also

- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avplayer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avplayer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests the invocation of a block when specified times are traversed during normal playback.
- [func removeTimeObserver(Any)](avplayer/removetimeobserver(_:).md)
  Cancels a previously registered periodic or boundary time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/currenttime())*