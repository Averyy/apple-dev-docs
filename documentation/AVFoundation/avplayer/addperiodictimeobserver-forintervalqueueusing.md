# addPeriodicTimeObserver(forInterval:queue:using:)

**Framework**: AVFoundation  
**Kind**: method

Requests the periodic invocation of a given block during playback to report changing time.

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
func addPeriodicTimeObserver(forInterval interval: CMTime, queue: dispatch_queue_t?, using block: @escaping (CMTime) -> Void) -> Any
```

## Mentions

- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md)

#### Return Value

An opaque object that you pass as the argument to [`removeTimeObserver(_:)`](avplayer/removetimeobserver(_:).md) to cancel observation.

#### Discussion

You must maintain a strong reference to the returned value as long as you want the time observer to be invoked by the player. You must pair each invocation of this method with a corresponding call to [`removeTimeObserver(_:)`](avplayer/removetimeobserver(_:).md). Releasing the observer object without invoking [`removeTimeObserver(_:)`](avplayer/removetimeobserver(_:).md) results in undefined behavior.

The system invokes the block periodically at the interval specified, interpreted according to the timeline of the current item. It also invokes the block whenever time jumps or playback starts or stops. If the interval corresponds to a very short interval in real time, the player may invoke the block less frequently than your app requested. Even so, the player will invoke the block sufficiently often for the client to update indications of the current time appropriately in its end-user interface.

The following example illustrates how you set up a callback the system invokes every half second during normal playback.

> ❗ **Important**:  Use a `weak` reference to `self` in the callback block to prevent creating a retain cycle.

## Parameters

- `interval`: The time interval at which the system invokes the block during normal playback, according to progress of the player’s current time.
- `queue`: If you pass  , the system uses the main queue.
- `block`: The block takes a single parameter:

## See Also

- [func currentTime() -> CMTime](avplayer/currenttime.md)
  Returns the current time of the current player item.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avplayer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests the invocation of a block when specified times are traversed during normal playback.
- [func removeTimeObserver(Any)](avplayer/removetimeobserver(_:).md)
  Cancels a previously registered periodic or boundary time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/addperiodictimeobserver(forinterval:queue:using:))*