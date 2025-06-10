# MPMusicRepeatMode

**Framework**: Media Player  
**Kind**: enum

The repeat modes for the media player.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPMusicRepeatMode
```

## Topics

### Constants
- [MPMusicRepeatMode.default](mpmusicrepeatmode/default.md)
  The user’s preferred repeat mode.
- [MPMusicRepeatMode.none](mpmusicrepeatmode/none.md)
  The music player will not repeat the current song or playlist.
- [MPMusicRepeatMode.one](mpmusicrepeatmode/one.md)
  The music player will repeat the current song.
- [MPMusicRepeatMode.all](mpmusicrepeatmode/all.md)
  The music player will repeat the current playlist.
### Initializers
- [init?(rawValue: Int)](mpmusicrepeatmode/init(rawvalue:).md)

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
- [enum MPMusicPlaybackState](mpmusicplaybackstate.md)
  The music player playback state modes.
- [enum MPMusicShuffleMode](mpmusicshufflemode.md)
  The shuffle modes for the media player.
- [var volume: Float](mpmusicplayercontroller/volume.md)
  The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode)*