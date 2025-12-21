# BaseEquipmentState

**Framework**: TabletopKit  
**Kind**: struct

A state for equipment that contains no equipment-specific data.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct BaseEquipmentState
```

## Topics

### Creating an equipment state
- [init(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](baseequipmentstate/init(parentid:seatcontrol:pose:boundingbox:).md)
  Creates a base state for equipment using a parent, location, and player interactions.
- [init(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](baseequipmentstate/init(parentid:seatcontrol:pose:entity:).md)
### Getting the parent equipment
- [var parentID: EquipmentIdentifier](baseequipmentstate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
### Rendering the equipment
- [var boundingBox: Rect3D](baseequipmentstate/boundingbox.md)
  A 3D bounding box that encloses the equipment.
- [var pose: TableVisualState.Pose2D](baseequipmentstate/pose.md)
  The 2D position and rotation of the equipment relative to the equipment parent, or table.
### Controlling the equipment
- [var lockedBy: PlayerIdentifier?](baseequipmentstate/lockedby.md)
  The identifier for the player who exclusively controls the equipment.
- [var seatControl: ControllingSeats](baseequipmentstate/seatcontrol.md)
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
- [protocol CustomEquipmentState](customequipmentstate.md)
  A specialized protocol for the equipment state that allows to accommodate custom data that TabletopKit syncs between players.
- [protocol MutableEquipmentState](mutableequipmentstate.md)
  A protocol for equipment data that TabletopKit syncs between players, and that can be mutated.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/baseequipmentstate)*