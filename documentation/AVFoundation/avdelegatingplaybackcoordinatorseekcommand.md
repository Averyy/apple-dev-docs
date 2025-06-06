# AVDelegatingPlaybackCoordinatorSeekCommand

**Framework**: AVFoundation  
**Kind**: class

A command that indicates to seek to a new time in the item timeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinatorSeekCommand
```

## Topics

### Accessing Command Details
- [var shouldBufferInAnticipationOfPlayback: Bool](avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback.md)
  A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.
- [var anticipatedPlaybackRate: Float](avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate.md)
  The rate at which the coordinator expects playback to resume.
- [var itemTime: CMTime](avdelegatingplaybackcoordinatorseekcommand/itemtime.md)
  The time to seek to in the item timeline.
- [var completionDueDate: Date?](avdelegatingplaybackcoordinatorseekcommand/completionduedate.md)
  The deadline by which the coordinator expects the delegate to handle the command.

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

## See Also

- [class AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
  An abstract superclass for playback commands.
- [class AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md)
  A command that indicates to play at a specific rate and time.
- [class AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md)
  A command that indicates to pause playback.
- [class AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
  A command that indicates to start buffering data in preparation for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand)*