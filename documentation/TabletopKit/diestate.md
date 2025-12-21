# DieState

**Framework**: TabletopKit  
**Kind**: struct

A state for dice that contains the current value.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct DieState
```

## Topics

### Creating a die state
- [init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](diestate/init(value:parentid:seatcontrol:pose:boundingbox:).md)
  Creates the state of a die using the specified current value, location, and player interactions.
- [init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](diestate/init(value:parentid:seatcontrol:pose:entity:).md)
  Creates a die state with the given die value, parent, controlling seats, pose, and associated entity providing the bounding box.
### Getting the die data
- [var value: Int](diestate/value.md)
  The numerical value that appears on the top face of the die.
### Getting the parent equipment
- [var parentID: EquipmentIdentifier](diestate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
### Rendering the equipment
- [var boundingBox: Rect3D](diestate/boundingbox.md)
  A 3D bounding box that encloses the die.
- [var pose: TableVisualState.Pose2D](diestate/pose.md)
  The 2D position and rotation of the equipment relative to the equipment parent, or table.
### Controlling the equipment
- [var lockedBy: PlayerIdentifier?](diestate/lockedby.md)
  The identifier for the player who exclusively controls the equipment.
- [var seatControl: ControllingSeats](diestate/seatcontrol.md)
  The seats that can manipulate or interact with the equipment.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [EquipmentState](equipmentstate.md)
- [MutableEquipmentState](mutableequipmentstate.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing playing card overlap and physical characteristics](implementing-playing-card-overlap-and-physical-characteristics.md)
  Add interactive card game behavior for a pile of playing cards with physically realistic stacking and overlapping.
- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [struct EquipmentCollection](equipmentcollection.md)
  A collection of equipment whose state can be inspected and modified.
- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
- [struct EquipmentStateCollection](equipmentstatecollection.md)
  A collection of equipment states that can be inspected and modified.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [protocol CustomEquipmentState](customequipmentstate.md)
  A specialized protocol for the equipment state that allows to accommodate custom data that TabletopKit syncs between players.
- [protocol MutableEquipmentState](mutableequipmentstate.md)
  A protocol for equipment data that TabletopKit syncs between players, and that can be mutated.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/diestate)*