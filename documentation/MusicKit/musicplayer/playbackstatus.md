# MusicPlayer.PlaybackStatus

**Framework**: MusicKit  
**Kind**: enum

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

You determine a music player’s state by checking the [`playbackStatus`](musicplayer/state-swift.class/playbackstatus.md) property. Depending on the property’s value, you can update your app’s user interface or take other appropriate action.

## Topics

### Operators
- [static func == (MusicPlayer.PlaybackStatus, MusicPlayer.PlaybackStatus) -> Bool](musicplayer/playbackstatus/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MusicPlayer.PlaybackStatus.interrupted](musicplayer/playbackstatus/interrupted.md)
  The music player is in an interrupted state, such as from an incoming phone call.
- [MusicPlayer.PlaybackStatus.paused](musicplayer/playbackstatus/paused.md)
  The music player is in a paused state.
- [MusicPlayer.PlaybackStatus.playing](musicplayer/playbackstatus/playing.md)
  The music player is playing.
- [MusicPlayer.PlaybackStatus.seekingBackward](musicplayer/playbackstatus/seekingbackward.md)
  The music player is seeking backward.
- [MusicPlayer.PlaybackStatus.seekingForward](musicplayer/playbackstatus/seekingforward.md)
  The music player is seeking forward.
- [MusicPlayer.PlaybackStatus.stopped](musicplayer/playbackstatus/stopped.md)
  The music player is in a stopped state.
### Instance Properties
- [var hashValue: Int](musicplayer/playbackstatus/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](musicplayer/playbackstatus/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](musicplayer/playbackstatus/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/playbackstatus)*