# playheadReachedLiveEdge

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Indicates that the player automatically switched the playback rate from > 1.0 back to 1.0 when the playhead reached the live edge during live streaming.

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
static let playheadReachedLiveEdge: AVPlayer.RateDidChangeReason
```

```c
extern AVPlayerRateDidChangeReason const AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge;
```

## See Also

### Controlling playback
- [var defaultRate: Float](../defaultrate.md)
  A default rate at which to begin playback.
- [func play()](../play%28%29.md)
  Begins playback of the current item.
- [func pause()](../pause%28%29.md)
  Pauses playback of the current item.
- [var rate: Float](../rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](../ratedidchangenotification.md)
  A notification that a player posts when its rate changes.
- [static let reversePlaybackReachedStartOfSeekableRange: AVPlayer.RateDidChangeReason](./reverseplaybackreachedstartofseekablerange.md)
  Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/playheadreachedliveedge)*