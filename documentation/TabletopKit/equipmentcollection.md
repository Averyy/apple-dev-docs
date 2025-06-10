# EquipmentCollection

**Framework**: TabletopKit  
**Kind**: struct

A collection of equipment whose state can be inspected and modified.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct EquipmentCollection
```

## Topics

### Instance Properties
- [var count: Int](equipmentcollection/count.md)
  The number of equipment items in this collection.
- [var ids: [EquipmentIdentifier]](equipmentcollection/ids.md)
  The identifiers of all the equipment in this collection.
- [var state: EquipmentStateCollection](equipmentcollection/state.md)
  The collection of equipment states.
### Instance Methods
- [func ids(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](equipmentcollection/ids(childrenof:).md)
  Returns the identifiers of all equipment that are children of the given equipment identifier.
- [func ids(descendantsOf: EquipmentIdentifier) -> [EquipmentIdentifier]](equipmentcollection/ids(descendantsof:).md)
  Returns the identifiers of all equipment that are descendants of the given equipment identifier.
- [func ids(of: (some Equipment).Type) -> [EquipmentIdentifier]](equipmentcollection/ids(of:).md)
  Returns the identifiers of all equipment that conform to the given type.
- [func reparent(id: EquipmentIdentifier, to: EquipmentIdentifier)](equipmentcollection/reparent(id:to:).md)
  Change the parent of the equipment matching the given identifier. The given equipment becomes the last of the parent’s children.
- [func reparent(ids: [EquipmentIdentifier], to: EquipmentIdentifier)](equipmentcollection/reparent(ids:to:).md)
  Change the parent of the equipment matching the given identifiers. The reparented equipment is appended at the end of the parent’s children.
### Subscripts
- [subscript<E>(of _: E.Type) -> [(identifier: EquipmentIdentifier, state: E.State)]](equipmentcollection/subscript(of:).md)
  Returns the identifiers and corresponding states of all equipment that conform to the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection)*