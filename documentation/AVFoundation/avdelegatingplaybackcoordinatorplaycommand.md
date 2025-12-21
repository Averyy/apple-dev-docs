# AVDelegatingPlaybackCoordinatorPlayCommand

**Framework**: AVFoundation  
**Kind**: class

A command that indicates to play at a specific rate and time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinatorPlayCommand
```

## Topics

### Accessing command details
- [var rate: Float](avdelegatingplaybackcoordinatorplaycommand/rate.md)
  A rate to use when starting playback.
- [var itemTime: CMTime](avdelegatingplaybackcoordinatorplaycommand/itemtime.md)
  A time in the item timeline to use to begin playback.
- [var hostClockTime: CMTime](avdelegatingplaybackcoordinatorplaycommand/hostclocktime.md)
  A host clock time to use to begin playback.

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
- [class AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md)
  A command that indicates to pause playback.
- [class AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)
  A command that indicates to seek to a new time in the item timeline.
- [class AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
  A command that indicates to start buffering data in preparation for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand)*