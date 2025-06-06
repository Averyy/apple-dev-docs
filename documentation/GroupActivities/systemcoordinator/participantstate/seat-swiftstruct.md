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

### Operators
- [static func == (SystemCoordinator.ParticipantState.Seat, SystemCoordinator.ParticipantState.Seat) -> Bool](systemcoordinator/participantstate/seat-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](systemcoordinator/participantstate/seat-swift.struct/hashvalue.md)
  The hash value.
- [let pose: Pose3D](systemcoordinator/participantstate/seat-swift.struct/pose.md)
  The position and rotation of the seat.
- [let role: (any SpatialTemplateRole)?](systemcoordinator/participantstate/seat-swift.struct/role.md)
  The role attached to this seat, if any.
### Instance Methods
- [func hash(into: inout Hasher)](systemcoordinator/participantstate/seat-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](systemcoordinator/participantstate/seat-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate/seat-swift.struct)*