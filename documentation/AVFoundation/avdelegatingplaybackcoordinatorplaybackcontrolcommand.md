# AVDelegatingPlaybackCoordinatorPlaybackControlCommand

**Framework**: AVFoundation  
**Kind**: class

An abstract superclass for playback commands.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinatorPlaybackControlCommand
```

#### Overview

Playback commands inherit state that identifies their originator and applicable item.

## Topics

### Accessing Command Details
- [var expectedCurrentItemIdentifier: String](avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md)
  An item identifier the coordinator issues the command for.
- [var originator: AVCoordinatedPlaybackParticipant?](avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator.md)
  The participant that causes the coordinator to issue the command.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
- [AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md)
- [AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md)
- [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md)
  A command that indicates to play at a specific rate and time.
- [class AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md)
  A command that indicates to pause playback.
- [class AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)
  A command that indicates to seek to a new time in the item timeline.
- [class AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
  A command that indicates to start buffering data in preparation for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand)*