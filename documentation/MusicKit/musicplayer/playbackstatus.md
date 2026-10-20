# MusicPlayer.PlaybackStatus

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

The music player playback status modes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PlaybackStatus
```

#### Overview

You determine a music player’s state by checking the [`playbackStatus`](./state-swift.class/playbackstatus.md) property. Depending on the property’s value, you can update your app’s user interface or take other appropriate action.

## Topics

### Enumeration Cases
- [MusicPlayer.PlaybackStatus.interrupted](./playbackstatus/interrupted.md)
  The music player is in an interrupted state, such as from an incoming phone call.
- [MusicPlayer.PlaybackStatus.paused](./playbackstatus/paused.md)
  The music player is in a paused state.
- [MusicPlayer.PlaybackStatus.playing](./playbackstatus/playing.md)
  The music player is playing.
- [MusicPlayer.PlaybackStatus.seekingBackward](./playbackstatus/seekingbackward.md)
  The music player is seeking backward.
- [MusicPlayer.PlaybackStatus.seekingForward](./playbackstatus/seekingforward.md)
  The music player is seeking forward.
- [MusicPlayer.PlaybackStatus.stopped](./playbackstatus/stopped.md)
  The music player is in a stopped state.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/playbackstatus)*