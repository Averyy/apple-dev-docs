# applicationQueuePlayer

**Framework**: Media Player  
**Kind**: property

Returns the application queue music player.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var applicationQueuePlayer: MPMusicPlayerApplicationController { get }
```

#### Return Value

The application queue music player.

#### Discussion

The application queue music player plays music locally within your app. The application queue music player provides more functionality and greater control over the music played than the application music player.

The music player doesn’t affect the Music app’s state. When your app moves to the background, the music player stops playing the current media.

## See Also

- [class var applicationMusicPlayer: MPMusicPlayerController](mpmusicplayercontroller/applicationmusicplayer.md)
  Returns the application music player.
- [class var systemMusicPlayer: any MPMusicPlayerController & MPSystemMusicPlayerController](mpmusicplayercontroller/systemmusicplayer.md)
  Returns the system music player, which controls the Music app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/applicationqueueplayer)*