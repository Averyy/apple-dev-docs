# volume

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: To provide UI for adjusting system playback volume, use the [`MPVolumeView`](../mpvolumeview.md) class, which provides media playback controls that iOS users expect and whose appearance you can customize.

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property (nonatomic) float volume;
```

## See Also

### Managing playback mode and state
- [var nowPlayingItem: MPMediaItem?](./nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var indexOfNowPlayingItem: Int](./indexofnowplayingitem.md)
  The index of the now playing item in the current playback queue.
- [var playbackState: MPMusicPlaybackState](./playbackstate.md)
  The current playback state of the music player.
- [var repeatMode: MPMusicRepeatMode](./repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MPMusicShuffleMode](./shufflemode.md)
  The current shuffle mode of the music player.
- [enum MPMusicPlaybackState](../mpmusicplaybackstate.md)
  The music player playback state modes.
- [enum MPMusicRepeatMode](../mpmusicrepeatmode.md)
  The repeat modes for the media player.
- [enum MPMusicShuffleMode](../mpmusicshufflemode.md)
  The shuffle modes for the media player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/volume)*