# systemMusicPlayer

**Framework**: Media Player  
**Kind**: property

Returns the system music player, which controls the Music app’s state.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var systemMusicPlayer: any MPMusicPlayerController & MPSystemMusicPlayerController { get }
```

#### Return Value

The system music player.

#### Discussion

The System music player employs the Music app on your behalf. On instantiation, it takes on the current Music app state and controls that state as your app runs. Specifically, the shared state includes the following:

- Repeat mode (see [`MPMusicRepeatMode`](mpmusicrepeatmode.md))
- Shuffle mode (see [`MPMusicShuffleMode`](mpmusicshufflemode.md))
- Now-playing item (see [`nowPlayingItem`](mpmusicplayercontroller/nowplayingitem.md))
- Playback state (see [`playbackState`](mpmusicplayercontroller/playbackstate.md))

Other aspects of the Music app’s state aren’t shared. Music that’s playing continues to play when your app moves to the background.

## See Also

- [class var applicationMusicPlayer: MPMusicPlayerController](mpmusicplayercontroller/applicationmusicplayer.md)
  Returns the application music player.
- [class var applicationQueuePlayer: MPMusicPlayerApplicationController](mpmusicplayercontroller/applicationqueueplayer.md)
  Returns the application queue music player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/systemmusicplayer)*