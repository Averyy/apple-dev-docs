# defaultRate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A default rate at which to begin playback.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
var defaultRate: Float { get set }
```

```objc
@property (nonatomic) float defaultRate;
```

## Mentions

- [Controlling the transport behavior of a player](../controlling-the-transport-behavior-of-a-player.md)

## Discussion

This value represents the default playback rate the player uses when you call its [`play()`](./play%28%29.md) method. After playback begins, the rate may differ from the default if you modify the player’s [`rate`](./rate.md) value, such as by calling [`pause()`](./pause%28%29.md).

> ❗ **Important**:  Begin playback by calling the [`play()`](./play%28%29.md) method. Don’t start playback by setting the [`rate`](./rate.md) property value to `1.0`. Instead, use [`rate`](./rate.md) to make immediate, temporary changes to the playback rate. The next time you call the [`play()`](./play%28%29.md) method, the player restores the rate to the value of [`defaultRate`](./defaultrate.md).

## See Also

### Controlling playback
- [func play()](./play%28%29.md)
  Begins playback of the current item.
- [func pause()](./pause%28%29.md)
  Pauses playback of the current item.
- [var rate: Float](./rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](./ratedidchangenotification.md)
  A notification that a player posts when its rate changes.
- [static let playheadReachedLiveEdge: AVPlayer.RateDidChangeReason](./ratedidchangereason/playheadreachedliveedge.md)
  Indicates that the player automatically switched the playback rate from > 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [static let reversePlaybackReachedStartOfSeekableRange: AVPlayer.RateDidChangeReason](./ratedidchangereason/reverseplaybackreachedstartofseekablerange.md)
  Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/defaultrate)*