# subscript(id:)

**Framework**: TabletopKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns and/or modifies the state for the equipment with given identifier.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
subscript(id equipmentID: EquipmentIdentifier) -> (any MutableEquipmentState)? { get set }
```

## See Also

### Accessing the subscript
- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](./subscript%28ids%29.md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, id _: EquipmentIdentifier) -> E.State?](./subscript%28of,id%29.md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.
- [subscript<E>(of _: E.Type, ids _: some Sequence<EquipmentIdentifier>) -> [E.State?]](./subscript%28of,ids%29.md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection/subscript(id:))*