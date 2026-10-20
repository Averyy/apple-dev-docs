# ids(descendantsOf:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifiers of all equipment that are descendants of the given equipment identifier.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func ids(descendantsOf parentID: EquipmentIdentifier) -> [EquipmentIdentifier]
```

## Parameters

- `parentID`: The equipment identifier whose descendants should be returned.

## See Also

### Retrieving equipment identifiers
- [func ids(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](./ids%28childrenof%29.md)
  Returns the identifiers of all equipment that are children of the given equipment identifier.
- [func ids(of: (some Equipment).Type) -> [EquipmentIdentifier]](./ids%28of%29.md)
  Returns the identifiers of all equipment that conform to the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/ids(descendantsof:))*