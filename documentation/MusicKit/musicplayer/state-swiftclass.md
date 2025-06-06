# MusicPlayer.State

**Framework**: MusicKit  
**Kind**: class

An object that exposes the observable properties of a music player.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class State
```

## Topics

### Instance Properties
- [var audioVariant: AudioVariant?](musicplayer/state-swift.class/audiovariant.md)
  The active variant that indicates the quality of audio for the current entry.
- [var objectWillChange: AnyPublisher<Void, Never>](musicplayer/state-swift.class/objectwillchange.md)
  A publisher that emits before the object has changed.
- [var playbackRate: Float](musicplayer/state-swift.class/playbackrate.md)
  The current playback rate for the player.
- [var playbackStatus: MusicPlayer.PlaybackStatus](musicplayer/state-swift.class/playbackstatus.md)
  The current playback status of the music player.
- [var repeatMode: MusicPlayer.RepeatMode?](musicplayer/state-swift.class/repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MusicPlayer.ShuffleMode?](musicplayer/state-swift.class/shufflemode.md)
  The current shuffle mode of the music player.
### Type Aliases
- [MusicPlayer.State.ObjectWillChangePublisher](musicplayer/state-swift.class/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.

## Relationships

### Conforms To
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/state-swift.class)*