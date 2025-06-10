# reparent(id:to:)

**Framework**: TabletopKit  
**Kind**: method

Change the parent of the equipment matching the given identifier. The given equipment becomes the last of the parent’s children.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func reparent(id: EquipmentIdentifier, to parent: EquipmentIdentifier)
```

## Parameters

- `id`: The identifier of the equipment to reparent.
- `parent`: The identifier of the new parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/reparent(id:to:))*