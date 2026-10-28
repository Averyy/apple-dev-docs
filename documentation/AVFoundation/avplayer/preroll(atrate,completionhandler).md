# preroll(atRate:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Begins loading media data to prime the media pipelines for playback.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func preroll(atRate rate: Float, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
nonisolated
func preroll(atRate rate: Float) async -> Bool
```

```objc
- (void) prerollAtRate:(float) rate completionHandler:(void (^)(BOOL finished)) completionHandler;
```

## Discussion

This method loads data starting at the item’s current playback time. The current rate for the playback item should always be 0 prior to calling this method. After the method calls the completion handler, you can change the item’s playback rate to begin playback.

If the player object is not ready to play (its [`status`](./status-swift.property.md) property is not [`AVPlayer.Status.readyToPlay`](./status-swift.enum/readytoplay.md)), this method throws an exception.

## Parameters

- `rate`: The playback rate to use when determining how much data to load.
- `completionHandler`: A block to execute when the player finishes the load attempt. This block takes a single Boolean parameter that contains [`true`](../../Swift/true.md) if the data was loaded or [`false`](../../Swift/false.md) if there was a problem. For example, the value might be [`false`](../../Swift/false.md) if the preroll was interrupted by a time change or incompatible rate change.

## See Also

### Synchronizing multiple players
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func cancelPendingPrerolls()](./cancelpendingprerolls%28%29.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](./sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](./masterclock.md)
  The host clock for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preroll(atrate:completionhandler:))*