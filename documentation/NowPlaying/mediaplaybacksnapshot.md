# MediaPlaybackSnapshot

**Framework**: Now Playing  
**Kind**: struct

A snapshot of playback state and timing for a Now Playing session.

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
struct MediaPlaybackSnapshot
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use a snapshot to describe whether the session is playing, paused, or buffering, along with the current elapsed time and the timestamp at which that elapsed time was captured. The system uses the snapshot to extrapolate elapsed time between updates.

## Topics

### Initializers
- [init(state: MediaPlaybackSnapshot.PlaybackState, defaultPlaybackRate: Float, elapsedTime: TimeInterval?, timestamp: Date?)](mediaplaybacksnapshot/init(state:defaultplaybackrate:elapsedtime:timestamp:).md)
  Creates a playback snapshot with the specified state and timing.
### Enumerations
- [MediaPlaybackSnapshot.PlaybackState](mediaplaybacksnapshot/playbackstate.md)
  The current playback state of a Now Playing session.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Content types and metadata](content-types-and-metadata.md)
  Describe the media your app is playing.
- [Playback commands](playback-commands.md)
  Declare the playback controls your app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot)*