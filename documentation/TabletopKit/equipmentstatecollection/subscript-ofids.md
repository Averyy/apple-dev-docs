# subscript(of:ids:)

**Framework**: TabletopKit  
**Kind**: subscript

Returns and/or modifies the state for the equipment with given identifier and matching type.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
subscript<E>(of type: E.Type, ids equipmentIDs: some Sequence<EquipmentIdentifier>) -> [E.State?] where E : Equipment { get set }
```

## Parameters

- `type`: The type of the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection/subscript(of:ids:))*