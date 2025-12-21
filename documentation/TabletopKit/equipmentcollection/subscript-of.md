# subscript(of:)

**Framework**: TabletopKit  
**Kind**: subscript

Returns the identifiers and corresponding states of all equipment that conform to the given type.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
subscript<E>(of type: E.Type) -> [(identifier: EquipmentIdentifier, state: E.State)] where E : Equipment { get }
```

## Parameters

- `type`: All returned equipment identifiers and states correspond to equipment of this given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/subscript(of:))*