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

- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentidentifier)*