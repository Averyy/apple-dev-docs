# iPodMusicPlayer

**Framework**: Media Player  
**Kind**: property

Returns the iPod music player, which controls the iPod app’s state.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class var iPodMusicPlayer: MPMusicPlayerController { get }
```

#### Return Value

The iPod music player.

#### Discussion

The iPod music player employs the iPod app on your behalf. On instantiation, it takes on the current iPod app state and controls that state as your app runs. Specifically, the shared state includes the following:

- Repeat mode (see [`MPMusicRepeatMode`](mpmusicrepeatmode.md))
- Shuffle mode (see [`MPMusicShuffleMode`](mpmusicshufflemode.md)
- Now-playing item (see [`nowPlayingItem`](mpmusicplayercontroller/nowplayingitem.md))
- Playback state (see [`playbackState`](mpmusicplayercontroller/playbackstate.md))

Other aspects of iPod state, such as the on-the-go playlist, aren’t shared. Music that’s playing continues to play when your app moves to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/ipodmusicplayer)*