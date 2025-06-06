# MPNowPlayingPlaybackState

**Framework**: Media Player  
**Kind**: enum

The playback state of the app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MPNowPlayingPlaybackState
```

## Topics

### Playback states
- [MPNowPlayingPlaybackState.unknown](mpnowplayingplaybackstate/unknown.md)
  The current state of the app is unknown.
- [MPNowPlayingPlaybackState.playing](mpnowplayingplaybackstate/playing.md)
  The app is currently playing a media item.
- [MPNowPlayingPlaybackState.paused](mpnowplayingplaybackstate/paused.md)
  The app is currently paused.
- [MPNowPlayingPlaybackState.stopped](mpnowplayingplaybackstate/stopped.md)
  The app has stopped playing.
- [MPNowPlayingPlaybackState.interrupted](mpnowplayingplaybackstate/interrupted.md)
  The app has been interrupted during playback.
### Initializers
- [init?(rawValue: UInt)](mpnowplayingplaybackstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var playbackState: MPNowPlayingPlaybackState](mpnowplayinginfocenter/playbackstate.md)
  The current playback state of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingplaybackstate)*