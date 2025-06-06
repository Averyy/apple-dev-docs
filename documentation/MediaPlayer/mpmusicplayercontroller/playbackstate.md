# playbackState

**Framework**: Media Player  
**Kind**: property

The current playback state of the music player.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var playbackState: MPMusicPlaybackState { get }
```

#### Discussion

If you configure a music player as a system music player, the playback state matches the playback state of the built-in Music app. This is true whether the Music app is using the device Music library or a home shared library. Note, however, that when the Music app is using a home shared library, the music player’s [`nowPlayingItem`](mpmusicplayercontroller/nowplayingitem.md) property is `nil`.

For the available playback states, see [`MPMusicPlaybackState`](mpmusicplaybackstate.md).

## See Also

- [var nowPlayingItem: MPMediaItem?](mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var indexOfNowPlayingItem: Int](mpmusicplayercontroller/indexofnowplayingitem.md)
  The index of the now playing item in the current playback queue.
- [var repeatMode: MPMusicRepeatMode](mpmusicplayercontroller/repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MPMusicShuffleMode](mpmusicplayercontroller/shufflemode.md)
  The current shuffle mode of the music player.
- [enum MPMusicPlaybackState](mpmusicplaybackstate.md)
  The music player playback state modes.
- [enum MPMusicRepeatMode](mpmusicrepeatmode.md)
  The repeat modes for the media player.
- [enum MPMusicShuffleMode](mpmusicshufflemode.md)
  The shuffle modes for the media player.
- [var volume: Float](mpmusicplayercontroller/volume.md)
  The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/playbackstate)*