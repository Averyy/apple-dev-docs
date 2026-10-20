# reparent(ids:to:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Change the parent of the equipment matching the given identifiers. The reparented equipment is appended at the end of the parent’s children.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func reparent(ids: [EquipmentIdentifier], to parent: EquipmentIdentifier)
```

## Parameters

- `ids`: The collection of equipment identifiers to corresponding to the equipment to reparent.
- `parent`: The identifier of the new parent.

## See Also

### Changing the parent
- [func reparent(id: EquipmentIdentifier, to: EquipmentIdentifier)](./reparent%28id,to%29.md)
  Change the parent of the equipment matching the given identifier. The given equipment becomes the last of the parent’s children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/reparent(ids:to:))*