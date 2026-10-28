# AVCoordinatedPlaybackParticipant

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that represents a participant in a coordinated playback session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVCoordinatedPlaybackParticipant
```

```objc
@interface AVCoordinatedPlaybackParticipant : NSObject
```

## Overview

Access the other participants in a session through the playback coordinator’s [`otherParticipants`](./avplaybackcoordinator/otherparticipants.md) property to determine their playback readiness and suspension reasons.

## Topics

### Accessing participant status
- [var identifier: UUID](./avcoordinatedplaybackparticipant/identifier.md)
  A unique identifier for the participant.
- [var isReadyToPlay: Bool](./avcoordinatedplaybackparticipant/isreadytoplay.md)
  A Boolean value that indicates whether the participant is ready to start coordinated playback.
- [var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason]](./avcoordinatedplaybackparticipant/suspensionreasons.md)
  The reasons a participant isn’t currently participating in coordinated playback.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Observing other participants
- [var otherParticipants: [AVCoordinatedPlaybackParticipant]](./avplaybackcoordinator/otherparticipants.md)
  The identifiers of the other participants in a group.
- [class let otherParticipantsDidChangeNotification: NSNotification.Name](./avplaybackcoordinator/otherparticipantsdidchangenotification.md)
  A notification that the coordinator posts when its other participants change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant)*