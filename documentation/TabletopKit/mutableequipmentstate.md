# MutableEquipmentState

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for equipment data that TabletopKit syncs between players, and that can be mutated.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MutableEquipmentState : EquipmentState
```

## Topics

### Instance Properties
- [var boundingBox: Rect3D](mutableequipmentstate/boundingbox.md)
  A 3D bounding box that encloses the equipment.
- [var parentID: EquipmentIdentifier](mutableequipmentstate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
- [var pose: TableVisualState.Pose2D](mutableequipmentstate/pose.md)
  The 2D position and rotation of the equipment relative to the parent equipment, or table.
- [var seatControl: ControllingSeats](mutableequipmentstate/seatcontrol.md)
  The seats that can manipulate or interact with this equipment.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [EquipmentState](equipmentstate.md)
### Inherited By
- [CustomEquipmentState](customequipmentstate.md)
### Conforming Types
- [BaseEquipmentState](baseequipmentstate.md)
- [CardState](cardstate.md)
- [DieState](diestate.md)
- [RawValueState](rawvaluestate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/mutableequipmentstate)*