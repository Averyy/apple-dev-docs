# otherParticipants

**Framework**: Avfoundation  
**Kind**: property

The identifiers of the other participants in a group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var otherParticipants: [AVCoordinatedPlaybackParticipant] { get }
```

#### Discussion

Use this property value to create a user interface that informs the user about the state of other participants in the group.

> **Note**:  To observe changes to this property value, register for notifications of type [`otherParticipantsDidChangeNotification`](avplaybackcoordinator/otherparticipantsdidchangenotification.md).

## See Also

- [class AVCoordinatedPlaybackParticipant](avcoordinatedplaybackparticipant.md)
  An object that represents a participant in a coordinated playback session.
- [class let otherParticipantsDidChangeNotification: NSNotification.Name](avplaybackcoordinator/otherparticipantsdidchangenotification.md)
  A notification that the coordinator posts when its other participants change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/otherparticipants)*