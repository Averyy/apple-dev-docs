# iPodMusicPlayer

**Framework**: Media Player  
**Kind**: property  
**Role**: Type Property

Returns the iPod music player, which controls the iPod app’s state.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The iPod app was renamed. Use the [`systemMusicPlayer`](./systemmusicplayer.md) method instead.

## Declaration

```swift
class var iPodMusicPlayer: MPMusicPlayerController { get }
```

```objc
@property (class, nonatomic, readonly) MPMusicPlayerController * iPodMusicPlayer;
```

#### Return Value

The iPod music player.

#### Discussion

The iPod music player employs the iPod app on your behalf. On instantiation, it takes on the current iPod app state and controls that state as your app runs. Specifically, the shared state includes the following:

- Repeat mode (see [`MPMusicRepeatMode`](../mpmusicrepeatmode.md))
- Shuffle mode (see [`MPMusicShuffleMode`](../mpmusicshufflemode.md)
- Now-playing item (see [`nowPlayingItem`](./nowplayingitem.md))
- Playback state (see [`playbackState`](./playbackstate.md))

Other aspects of iPod state, such as the on-the-go playlist, aren’t shared. Music that’s playing continues to play when your app moves to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/ipodmusicplayer)*