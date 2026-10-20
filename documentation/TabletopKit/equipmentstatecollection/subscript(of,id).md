# subscript(of:id:)

**Framework**: TabletopKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns and/or modifies the state for the equipment with given identifier and matching type.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
subscript<E>(of type: E.Type, id equipmentID: EquipmentIdentifier) -> E.State? where E : Equipment { get set }
```

## Parameters

- `type`: The type of the equipment.

## See Also

### Accessing the subscript
- [subscript(id _: EquipmentIdentifier) -> (any MutableEquipmentState)?](./subscript%28id%29.md)
  Returns and/or modifies the state for the equipment with given identifier.
- [subscript(ids _: some Sequence<EquipmentIdentifier>) -> [(any MutableEquipmentState)?]](./subscript%28ids%29.md)
  Returns and/or modifies the states for the equipment with given identifiers.
- [subscript<E>(of _: E.Type, ids _: some Sequence<EquipmentIdentifier>) -> [E.State?]](./subscript%28of,ids%29.md)
  Returns and/or modifies the state for the equipment with given identifier and matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection/subscript(of:id:))*