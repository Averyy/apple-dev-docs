# AVDelegatingPlaybackCoordinatorPauseCommand

**Framework**: AVFoundation  
**Kind**: class

A command that indicates to pause playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinatorPauseCommand
```

## Topics

### Accessing command details
- [var shouldBufferInAnticipationOfPlayback: Bool](avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.md)
  A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.
- [var anticipatedPlaybackRate: Float](avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate.md)
  The rate at which the coordinator expects the current item to play.

## Relationships

### Inherits From
- [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
  An abstract superclass for playback commands.
- [class AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md)
  A command that indicates to play at a specific rate and time.
- [class AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)
  A command that indicates to seek to a new time in the item timeline.
- [class AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
  A command that indicates to start buffering data in preparation for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand)*