# setRate(_:time:atHostTime:)

**Framework**: AVFoundation  
**Kind**: method

Synchronizes the playback rate and time of the current item with an external source.

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
func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)
```

#### Discussion

This method adjusts the current item’s timebase so that the time in `itemTime` is in sync with the time in `hostClockTime`. Thus, if `hostClockTime` specifies a time in the past, the item’s timebase is adjusted to make it appear as if the item has been running at the specified rate since `itemTime`. And if `hostClockTime` specifies a time in the future, playback is adjusted backward (if possible) so that the value in `itemTime` occurs at the precise moment the host’s clock reaches the value in `hostClockTime`. If there is no content to play before the time specified by `itemTime`, playback holds until the two times come into sync.

This method does not ensure that media data is loaded before the timebase starts moving. However, if you specify a host time in the near future, that would give you some time to load the media data and prepare for playback.

> ❗ **Important**:  This method is not currently supported for HTTP Live Streaming or when [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`true`](https://developer.apple.com/documentation/swift/true). For clients linked against iOS 10.0 and later or macOS 10.12 and later, invoking this method when [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`true`](https://developer.apple.com/documentation/swift/true) will raise an `NSInvalidArgument` exception.

## Parameters

- `rate`: The playback rate for the item.
- `itemTime`: The precise time at which to match playback of the item. To use the current item’s current time, specify  .
- `hostClockTime`: The host time at which to synchronize playback. If you specify  , the rate and time are set together without any external synchronization.

## See Also

- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](avplayer/preroll(atrate:completionhandler:).md)
  Begins loading media data to prime the media pipelines for playback.
- [func cancelPendingPrerolls()](avplayer/cancelpendingprerolls.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](avplayer/sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](avplayer/masterclock.md)
  The host clock for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/setrate(_:time:athosttime:))*