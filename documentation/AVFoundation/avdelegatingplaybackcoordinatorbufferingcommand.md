# AVDelegatingPlaybackCoordinatorBufferingCommand

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A command that indicates to start buffering data in preparation for playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinatorBufferingCommand
```

```objc
@interface AVDelegatingPlaybackCoordinatorBufferingCommand : AVDelegatingPlaybackCoordinatorPlaybackControlCommand
```

## Overview

When your app receives this command, update its user interface to indicate that playback is buffering.

## Topics

### Accessing command details
- [var anticipatedPlaybackRate: Float](./avdelegatingplaybackcoordinatorbufferingcommand/anticipatedplaybackrate.md)
  The rate at which the coordinator expects the current item to play.
- [var completionDueDate: Date?](./avdelegatingplaybackcoordinatorbufferingcommand/completionduedate.md)
  The deadline by which the coordinator expects the delegate to complete execution of a command.

## Relationships

### Inherits From
- [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](./avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Playback commands
- [class AVDelegatingPlaybackCoordinatorPlaybackControlCommand](./avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
  An abstract superclass for playback commands.
- [class AVDelegatingPlaybackCoordinatorPlayCommand](./avdelegatingplaybackcoordinatorplaycommand.md)
  A command that indicates to play at a specific rate and time.
- [class AVDelegatingPlaybackCoordinatorPauseCommand](./avdelegatingplaybackcoordinatorpausecommand.md)
  A command that indicates to pause playback.
- [class AVDelegatingPlaybackCoordinatorSeekCommand](./avdelegatingplaybackcoordinatorseekcommand.md)
  A command that indicates to seek to a new time in the item timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand)*