# MediaPlaybackSnapshot.PlaybackState

**Framework**: Now Playing  
**Kind**: enum  
**Role**: Enumeration

The current playback state of a Now Playing session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum PlaybackState
```

## Overview

Use this type to inform the system about the current state of media playback in your session. The system uses the playback state to update the Now Playing interface and manage audio session behavior appropriately.

## Topics

### Enumeration Cases
- [MediaPlaybackSnapshot.PlaybackState.buffering](./playbackstate/buffering.md)
  Playback is buffering content.
- [MediaPlaybackSnapshot.PlaybackState.interrupted](./playbackstate/interrupted.md)
  Playback was interrupted by the system.
- [MediaPlaybackSnapshot.PlaybackState.paused](./playbackstate/paused.md)
  Playback is paused.
- [MediaPlaybackSnapshot.PlaybackState.playing(rate:)](./playbackstate/playing%28rate%29.md)
  Content is currently playing.
- [MediaPlaybackSnapshot.PlaybackState.stopped](./playbackstate/stopped.md)
  Playback is stopped.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot/playbackstate)*