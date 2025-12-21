# EquipmentCollection

**Framework**: TabletopKit  
**Kind**: struct

A collection of equipment whose state can be inspected and modified.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct EquipmentCollection
```

## Topics

### Getting collection properties
- [var count: Int](equipmentcollection/count.md)
  The number of equipment items in this collection.
- [var ids: [EquipmentIdentifier]](equipmentcollection/ids.md)
  The identifiers of all the equipment in this collection.
- [var state: EquipmentStateCollection](equipmentcollection/state.md)
  The collection of equipment states.
### Retrieving equipment identifiers
- [func ids(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](equipmentcollection/ids(childrenof:).md)
  Returns the identifiers of all equipment that are children of the given equipment identifier.
- [func ids(descendantsOf: EquipmentIdentifier) -> [EquipmentIdentifier]](equipmentcollection/ids(descendantsof:).md)
  Returns the identifiers of all equipment that are descendants of the given equipment identifier.
- [func ids(of: (some Equipment).Type) -> [EquipmentIdentifier]](equipmentcollection/ids(of:).md)
  Returns the identifiers of all equipment that conform to the given type.
### Changing the parent
- [func reparent(id: EquipmentIdentifier, to: EquipmentIdentifier)](equipmentcollection/reparent(id:to:).md)
  Change the parent of the equipment matching the given identifier. The given equipment becomes the last of the parent’s children.
- [func reparent(ids: [EquipmentIdentifier], to: EquipmentIdentifier)](equipmentcollection/reparent(ids:to:).md)
  Change the parent of the equipment matching the given identifiers. The reparented equipment is appended at the end of the parent’s children.
### Accessing the subscript
- [subscript<E>(of _: E.Type) -> [(identifier: EquipmentIdentifier, state: E.State)]](equipmentcollection/subscript(of:).md)
  Returns the identifiers and corresponding states of all equipment that conform to the given type.

## See Also

- [Implementing playing card overlap and physical characteristics](implementing-playing-card-overlap-and-physical-characteristics.md)
  Add interactive card game behavior for a pile of playing cards with physically realistic stacking and overlapping.
- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
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
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection)*