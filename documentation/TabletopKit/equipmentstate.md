# EquipmentState

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for the equipment data that TabletopKit syncs between players.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EquipmentState : Equatable
```

## Topics

### Getting the parent equipment
- [var parentID: EquipmentIdentifier](equipmentstate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
### Rendering the equipment
- [var boundingBox: Rect3D](equipmentstate/boundingbox.md)
  A 3D bounding box that encloses the equipment.
- [var pose: TableVisualState.Pose2D](equipmentstate/pose.md)
  The 2D position and rotation of the equipment relative to the parent equipment, or table.
### Controlling the equipment
- [var lockedBy: PlayerIdentifier?](equipmentstate/lockedby.md)
  The identifier for the player who exclusively controls the equipment.
- [var seatControl: ControllingSeats](equipmentstate/seatcontrol.md)
  The seats that can manipulate or interact with this equipment.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
### Inherited By
- [CustomEquipmentState](customequipmentstate.md)
- [MutableEquipmentState](mutableequipmentstate.md)
### Conforming Types
- [BaseEquipmentState](baseequipmentstate.md)
- [CardState](cardstate.md)
- [DieState](diestate.md)
- [RawValueState](rawvaluestate.md)

## See Also

- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstate)*