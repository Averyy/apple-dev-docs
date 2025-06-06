# pause()

**Framework**: AVFoundation  
**Kind**: method

Pauses playback of the current item.

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
func pause()
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

Calling this method is the same as setting the [`rate`](avplayer/rate.md) to `0.0`.

## See Also

- [var defaultRate: Float](avplayer/defaultrate.md)
  A default rate at which to begin playback.
- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [var rate: Float](avplayer/rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](avplayer/ratedidchangenotification.md)
  A notification that a player posts when its rate changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/pause())*