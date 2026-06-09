# reversePlaybackReachedStartOfSeekableRange

**Framework**: AVFoundation  
**Kind**: property

Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
static let reversePlaybackReachedStartOfSeekableRange: AVPlayer.RateDidChangeReason
```

## See Also

- [var defaultRate: Float](avplayer/defaultrate.md)
  A default rate at which to begin playback.
- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [func pause()](avplayer/pause.md)
  Pauses playback of the current item.
- [var rate: Float](avplayer/rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](avplayer/ratedidchangenotification.md)
  A notification that a player posts when its rate changes.
- [static let playheadReachedLiveEdge: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/playheadreachedliveedge.md)
  Indicates that the player automatically switched the playback rate from > 1.0 back to 1.0 when the playhead reached the live edge during live streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange)*