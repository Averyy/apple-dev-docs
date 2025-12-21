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
- [case restrictedCurrent([TableSeatIdentifier])](controllingseats/restrictedcurrent(_:).md)
  Lets players in specific seats interact with the equipment if they are currently in turn.
- [ControllingSeats.inherited](controllingseats/inherited.md)
  The value is inherited from the parent. The table implicit value is considered to be `.any`.
- [ControllingSeats.current](controllingseats/current.md)
  Lets only seats currently in turn interact with the equipment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
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
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/controllingseats)*