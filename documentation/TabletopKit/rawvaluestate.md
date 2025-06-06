# RawValueState

**Framework**: TabletopKit  
**Kind**: struct

A state for equipment that contains a game-specific value.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct RawValueState
```

## Topics

### Creating a die state
- [init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](rawvaluestate/init(rawvalue:parentid:seatcontrol:pose:boundingbox:).md)
  Creates a state for equipment using the specified raw value, location, and player interactions.
- [init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](rawvaluestate/init(rawvalue:parentid:seatcontrol:pose:entity:).md)
### Getting the die data
- [var rawValue: UInt64](rawvaluestate/rawvalue.md)
  The integer value for this piece of equipment.
### Getting the parent equipment
- [var parentID: EquipmentIdentifier](rawvaluestate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
### Rendering the equipment
- [var boundingBox: Rect3D](rawvaluestate/boundingbox.md)
  A 3D bounding box that encloses the equipment.
- [var pose: TableVisualState.Pose2D](rawvaluestate/pose.md)
  The 2D position and rotation of the equipment relative to the equipment parent, or table.
### Controlling the equipment
- [var lockedBy: PlayerIdentifier?](rawvaluestate/lockedby.md)
  The identifier for the player who exclusively controls the equipment.
- [var seatControl: ControllingSeats](rawvaluestate/seatcontrol.md)
  The seats that can manipulate or interact with the equipment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [EquipmentState](equipmentstate.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/rawvaluestate)*