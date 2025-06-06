# indexOfNowPlayingItem

**Framework**: Media Player  
**Kind**: property

The index of the now playing item in the current playback queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var indexOfNowPlayingItem: Int { get }
```

#### Discussion

This property’s value is `NSNotFound` if the index isn’t valid, for example, if the playback queue is empty.

## See Also

- [var nowPlayingItem: MPMediaItem?](mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var playbackState: MPMusicPlaybackState](mpmusicplayercontroller/playbackstate.md)
  The current playback state of the music player.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/indexofnowplayingitem)*