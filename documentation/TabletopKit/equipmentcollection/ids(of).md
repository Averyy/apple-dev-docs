# ids(of:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifiers of all equipment that conform to the given type.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func ids(of type: (some Equipment).Type) -> [EquipmentIdentifier]
```

## Parameters

- `type`: All returned equipment identifiers correspond to equipment of this given type.

## See Also

### Retrieving equipment identifiers
- [func ids(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](./ids%28childrenof%29.md)
  Returns the identifiers of all equipment that are children of the given equipment identifier.
- [func ids(descendantsOf: EquipmentIdentifier) -> [EquipmentIdentifier]](./ids%28descendantsof%29.md)
  Returns the identifiers of all equipment that are descendants of the given equipment identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/ids(of:))*