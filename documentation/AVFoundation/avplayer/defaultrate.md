# defaultRate

**Framework**: AVFoundation  
**Kind**: property

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

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

This value represents the default playback rate the player uses when you call its [`play()`](avplayer/play().md) method. After playback begins, the rate may differ from the default if you modify the player’s [`rate`](avplayer/rate.md) value, such as by calling [`pause()`](avplayer/pause().md).

> ❗ **Important**:  Begin playback by calling the [`play()`](avplayer/play().md) method. Don’t start playback by setting the [`rate`](avplayer/rate.md) property value to `1.0`. Instead, use [`rate`](avplayer/rate.md) to make immediate, temporary changes to the playback rate. The next time you call the [`play()`](avplayer/play().md) method, the player restores the rate to the value of [`defaultRate`](avplayer/defaultrate.md).

## See Also

- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [func pause()](avplayer/pause.md)
  Pauses playback of the current item.
- [var rate: Float](avplayer/rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](avplayer/ratedidchangenotification.md)
  A notification that a player posts when its rate changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/defaultrate)*