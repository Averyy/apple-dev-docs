# cancelPendingPrerolls()

**Framework**: AVFoundation  
**Kind**: method

Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.

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
func cancelPendingPrerolls()
```

#### Discussion

This method cancels and releases the completion handlers for any pending prerolls. The finished parameter of the completion handlers passed to [`preroll(atRate:completionHandler:)`](avplayer/preroll(atrate:completionhandler:).md) will be set to `false`.

## See Also

- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avplayer/setrate(_:time:athosttime:).md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](avplayer/preroll(atrate:completionhandler:).md)
  Begins loading media data to prime the media pipelines for playback.
- [var sourceClock: CMClock?](avplayer/sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](avplayer/masterclock.md)
  The host clock for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/cancelpendingprerolls())*