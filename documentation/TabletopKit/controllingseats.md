# ControllingSeats

**Framework**: TabletopKit  
**Kind**: enum

The seats that can manipulate or interact with the equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum ControllingSeats
```

## Topics

### Seats
- [ControllingSeats.any](controllingseats/any.md)
  Lets players in all seats interact with the equipment.
- [case restricted([TableSeatIdentifier])](controllingseats/restricted(_:).md)
  Lets players in specific seats interact with the equipment.
- [ControllingSeats.inherited](controllingseats/inherited.md)
  The value is inherited from the parent. The table implicit value is considered to be `.any`.
- [ControllingSeats.current](controllingseats/current.md)
  Lets only seats currently in turn interact with the equipment.
### Enumeration Cases
- [case restrictedCurrent([TableSeatIdentifier])](controllingseats/restrictedcurrent(_:).md)
  Lets players in specific seats interact with the equipment if they are currently in turn.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/controllingseats)*