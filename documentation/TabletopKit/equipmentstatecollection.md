# EquipmentStateCollection

**Framework**: TabletopKit  
**Kind**: struct

A collection of equipment states that can be inspected and modified.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct EquipmentStateCollection
```

## Topics

### Subscripts
- [subscript(id _: EquipmentIdentifier) -> (any MutableEquipmentState)?](equipmentstatecollection/subscript(id:).md)
  Returns and/or modifies the state for the equipment with given identifier.
- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](equipmentstatecollection/subscript(ids:).md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, id _: EquipmentIdentifier) -> E.State?](equipmentstatecollection/subscript(of:id:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.
- [subscript<E>(of _: E.Type, ids _: some Sequence<EquipmentIdentifier>) -> [E.State?]](equipmentstatecollection/subscript(of:ids:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection)*