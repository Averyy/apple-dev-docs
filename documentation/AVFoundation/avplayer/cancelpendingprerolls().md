# cancelPendingPrerolls()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancelPendingPrerolls;
```

## Discussion

This method cancels and releases the completion handlers for any pending prerolls. The finished parameter of the completion handlers passed to [`preroll(atRate:completionHandler:)`](./preroll%28atrate,completionhandler%29.md) will be set to `false`.

## See Also

### Synchronizing multiple players
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](./preroll%28atrate,completionhandler%29.md)
  Begins loading media data to prime the media pipelines for playback.
- [var sourceClock: CMClock?](./sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](./masterclock.md)
  The host clock for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/cancelpendingprerolls())*