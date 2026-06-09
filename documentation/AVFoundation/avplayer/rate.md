# rate

**Framework**: AVFoundation  
**Kind**: property

The current playback rate.

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
var rate: Float { get set }
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)

## See Also

- [var defaultRate: Float](avplayer/defaultrate.md)
  A default rate at which to begin playback.
- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [func pause()](avplayer/pause.md)
  Pauses playback of the current item.
- [class let rateDidChangeNotification: NSNotification.Name](avplayer/ratedidchangenotification.md)
  A notification that a player posts when its rate changes.
- [static let playheadReachedLiveEdge: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/playheadreachedliveedge.md)
  Indicates that the player automatically switched the playback rate from > 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [static let reversePlaybackReachedStartOfSeekableRange: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange.md)
  Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/rate)*