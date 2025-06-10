# MPMusicPlaybackState

**Framework**: Media Player  
**Kind**: enum

The music player playback state modes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPMusicPlaybackState
```

#### Overview

You determine a music player’s state by checking the [`playbackState`](mpmusicplayercontroller/playbackstate.md) property. Depending on the property’s value, you can update your application’s user interface or take other appropriate action.

## Topics

### Constants
- [MPMusicPlaybackState.stopped](mpmusicplaybackstate/stopped.md)
  The music player is stopped.
- [MPMusicPlaybackState.playing](mpmusicplaybackstate/playing.md)
  The music player is playing.
- [MPMusicPlaybackState.paused](mpmusicplaybackstate/paused.md)
  The music player is paused.
- [MPMusicPlaybackState.interrupted](mpmusicplaybackstate/interrupted.md)
  The music player has been interrupted, such as by an incoming phone call.
- [MPMusicPlaybackState.seekingForward](mpmusicplaybackstate/seekingforward.md)
  The music player is seeking forward.
- [MPMusicPlaybackState.seekingBackward](mpmusicplaybackstate/seekingbackward.md)
  The music player is seeking backward.
### Initializers
- [init?(rawValue: Int)](mpmusicplaybackstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var nowPlayingItem: MPMediaItem?](mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var indexOfNowPlayingItem: Int](mpmusicplayercontroller/indexofnowplayingitem.md)
  The index of the now playing item in the current playback queue.
- [var playbackState: MPMusicPlaybackState](mpmusicplayercontroller/playbackstate.md)
  The current playback state of the music player.
- [var repeatMode: MPMusicRepeatMode](mpmusicplayercontroller/repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MPMusicShuffleMode](mpmusicplayercontroller/shufflemode.md)
  The current shuffle mode of the music player.
- [enum MPMusicRepeatMode](mpmusicrepeatmode.md)
  The repeat modes for the media player.
- [enum MPMusicShuffleMode](mpmusicshufflemode.md)
  The shuffle modes for the media player.
- [var volume: Float](mpmusicplayercontroller/volume.md)
  The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate)*