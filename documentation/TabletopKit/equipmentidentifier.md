# EquipmentIdentifier

**Framework**: TabletopKit  
**Kind**: struct

A unique identifier for equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct EquipmentIdentifier
```

#### Overview

The equipment identifier needs to be unique across all instances of the same tabletop game.

## Topics

### Creating equipment identifiers
- [init(Int)](equipmentidentifier/init(_:).md)
### Getting identifier values
- [let rawValue: Int](equipmentidentifier/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentidentifier)*