# applicationMusicPlayer

**Framework**: Media Player  
**Kind**: property

Returns the application music player.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var applicationMusicPlayer: MPMusicPlayerController { get }
```

#### Return Value

The application music player.

#### Discussion

The application music player plays music locally within your app. The music player doesn’t affect the Music app’s state. When your app moves to the background, the music player stops playing the current media.

## See Also

- [class var applicationQueuePlayer: MPMusicPlayerApplicationController](mpmusicplayercontroller/applicationqueueplayer.md)
  Returns the application queue music player.
- [class var systemMusicPlayer: any MPMusicPlayerController & MPSystemMusicPlayerController](mpmusicplayercontroller/systemmusicplayer.md)
  Returns the system music player, which controls the Music app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/applicationmusicplayer)*