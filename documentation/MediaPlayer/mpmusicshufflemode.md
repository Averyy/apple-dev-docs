# MPMusicShuffleMode

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

The shuffle modes for the media player.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPMusicShuffleMode
```

```c
enum MPMusicShuffleMode : NSInteger;
```

## Topics

### Constants
- [MPMusicShuffleMode.default](./mpmusicshufflemode/default.md)
  The user’s preferred shuffle mode.
- [MPMusicShuffleMode.off](./mpmusicshufflemode/off.md)
  The playlist is not shuffled.
- [MPMusicShuffleMode.songs](./mpmusicshufflemode/songs.md)
  The playlist is shuffled by song.
- [MPMusicShuffleMode.albums](./mpmusicshufflemode/albums.md)
  The playlist is shuffled by album.
### Initializers
- [init?(rawValue: Int)](./mpmusicshufflemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing playback mode and state
- [var nowPlayingItem: MPMediaItem?](./mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var indexOfNowPlayingItem: Int](./mpmusicplayercontroller/indexofnowplayingitem.md)
  The index of the now playing item in the current playback queue.
- [var playbackState: MPMusicPlaybackState](./mpmusicplayercontroller/playbackstate.md)
  The current playback state of the music player.
- [var repeatMode: MPMusicRepeatMode](./mpmusicplayercontroller/repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MPMusicShuffleMode](./mpmusicplayercontroller/shufflemode.md)
  The current shuffle mode of the music player.
- [enum MPMusicPlaybackState](./mpmusicplaybackstate.md)
  The music player playback state modes.
- [enum MPMusicRepeatMode](./mpmusicrepeatmode.md)
  The repeat modes for the media player.
- [var volume: Float](./mpmusicplayercontroller/volume.md)
  The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode)*