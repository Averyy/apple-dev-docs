# subscript(of:ids:)

**Framework**: TabletopKit  
**Kind**: subscript

Returns and/or modifies the state for the equipment with given identifier and matching type.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
subscript<E>(of type: E.Type, ids equipmentIDs: some Sequence<EquipmentIdentifier>) -> [E.State?] where E : Equipment { get set }
```

## Parameters

- `type`: The type of the equipment.

## See Also

- [subscript(id _: EquipmentIdentifier) -> (any MutableEquipmentState)?](equipmentstatecollection/subscript(id:).md)
  Returns and/or modifies the state for the equipment with given identifier.
- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](equipmentstatecollection/subscript(ids:).md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, id _: EquipmentIdentifier) -> E.State?](equipmentstatecollection/subscript(of:id:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection/subscript(of:ids:))*