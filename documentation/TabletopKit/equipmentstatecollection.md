# EquipmentStateCollection

**Framework**: TabletopKit  
**Kind**: struct

A collection of equipment states that can be inspected and modified.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct EquipmentStateCollection
```

## Topics

### Accessing the subscript
- [subscript(id _: EquipmentIdentifier) -> (any MutableEquipmentState)?](equipmentstatecollection/subscript(id:).md)
  Returns and/or modifies the state for the equipment with given identifier.
- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](equipmentstatecollection/subscript(ids:).md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, id _: EquipmentIdentifier) -> E.State?](equipmentstatecollection/subscript(of:id:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.
- [subscript<E>(of _: E.Type, ids _: some Sequence<EquipmentIdentifier>) -> [E.State?]](equipmentstatecollection/subscript(of:ids:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.

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

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection)*