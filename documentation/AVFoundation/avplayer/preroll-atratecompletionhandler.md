# preroll(atRate:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

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
func preroll(atRate rate: Float) async -> Bool
```

#### Discussion

This method loads data starting at the item’s current playback time. The current rate for the playback item should always be 0 prior to calling this method. After the method calls the completion handler, you can change the item’s playback rate to begin playback.

If the player object is not ready to play (its [`status`](avplayer/status-swift.property.md) property is not [`AVPlayer.Status.readyToPlay`](avplayer/status-swift.enum/readytoplay.md)), this method throws an exception.

## Parameters

- `rate`: The playback rate to use when determining how much data to load.
- `completionHandler`: A block to execute when the player finishes the load attempt. This block takes a single Boolean parameter that contains   if the data was loaded or   if there was a problem. For example, the value might be   if the preroll was interrupted by a time change or incompatible rate change.

## See Also

- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avplayer/setrate(_:time:athosttime:).md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func cancelPendingPrerolls()](avplayer/cancelpendingprerolls.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](avplayer/sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](avplayer/masterclock.md)
  The host clock for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preroll(atrate:completionhandler:))*