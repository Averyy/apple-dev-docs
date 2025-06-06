# SystemMusicPlayer

**Framework**: MusicKit  
**Kind**: class

An object your app uses to play music by controlling the Music app’s state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class SystemMusicPlayer
```

#### Overview

The system music player employs the Music app on your behalf. When your app accesses the system music player for the first time, it assumes the current Music app state and controls it as your app runs. The shared state includes the following:

- Repeat mode (see [`MusicPlayer.RepeatMode`](musicplayer/repeatmode.md))
- Shuffle mode (see [`MusicPlayer.ShuffleMode`](musicplayer/shufflemode.md))
- Playback status (see `MusicPlayer/PlaybackStatus`)

The system music player doesn’t share other aspects of the Music app’s state. Music that’s playing continues to play when your app moves to the background.

## Topics

### Instance Properties
- [var queue: MusicPlayer.Queue](systemmusicplayer/queue.md)
  The playback queue for the system music player.
### Type Properties
- [static let shared: SystemMusicPlayer](systemmusicplayer/shared.md)
  The shared system music player, which controls the Music app’s state.

## Relationships

### Inherits From
- [MusicPlayer](musicplayer.md)

## See Also

- [class ApplicationMusicPlayer](applicationmusicplayer.md)
  An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [class MusicPlayer](musicplayer.md)
  An object your app uses to play music.
- [protocol PlayableMusicItem](playablemusicitem.md)
  A set of properties that a music player uses to initiate playback for a music item.
- [struct PlayParameters](playparameters.md)
  An opaque object that represents parameters to initiate playback of a playable music item using a music player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/systemmusicplayer)*