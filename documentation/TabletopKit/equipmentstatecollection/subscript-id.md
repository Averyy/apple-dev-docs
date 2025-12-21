# subscript(id:)

**Framework**: TabletopKit  
**Kind**: subscript

Returns and/or modifies the state for the equipment with given identifier.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
subscript(id equipmentID: EquipmentIdentifier) -> (any MutableEquipmentState)? { get set }
```

## See Also

- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](equipmentstatecollection/subscript(ids:).md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, id _: EquipmentIdentifier) -> E.State?](equipmentstatecollection/subscript(of:id:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.
- [subscript<E>(of _: E.Type, ids _: some Sequence<EquipmentIdentifier>) -> [E.State?]](equipmentstatecollection/subscript(of:ids:).md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection/subscript(id:))*