# SystemCoordinator.ParticipantState.Seat

**Framework**: Group Activities  
**Kind**: struct

A seat assigned to a single participant in a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Seat
```

#### Overview

You can use this structure to inspect the initial position of a participant in your group activity and place UI elements near them.

## Topics

### Instance Properties
- [let pose: Pose3D](systemcoordinator/participantstate/seat-swift.struct/pose.md)
  The position and rotation of the seat.
- [let role: (any SpatialTemplateRole)?](systemcoordinator/participantstate/seat-swift.struct/role.md)
  The role attached to this seat, if any.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate/seat-swift.struct)*