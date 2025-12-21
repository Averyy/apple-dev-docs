# ids(childrenOf:)

**Framework**: TabletopKit  
**Kind**: method

Returns the identifiers of all equipment that are children of the given equipment identifier.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func ids(childrenOf parentID: EquipmentIdentifier) -> [EquipmentIdentifier]
```

## Parameters

- `parentID`: The equipment identifier whose children should be returned.

## See Also

- [func ids(descendantsOf: EquipmentIdentifier) -> [EquipmentIdentifier]](equipmentcollection/ids(descendantsof:).md)
  Returns the identifiers of all equipment that are descendants of the given equipment identifier.
- [func ids(of: (some Equipment).Type) -> [EquipmentIdentifier]](equipmentcollection/ids(of:).md)
  Returns the identifiers of all equipment that conform to the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/ids(childrenof:))*