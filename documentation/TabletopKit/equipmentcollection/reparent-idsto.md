# reparent(ids:to:)

**Framework**: TabletopKit  
**Kind**: method

Change the parent of the equipment matching the given identifiers. The reparented equipment is appended at the end of the parent’s children.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func reparent(ids: [EquipmentIdentifier], to parent: EquipmentIdentifier)
```

## Parameters

- `ids`: The collection of equipment identifiers to corresponding to the equipment to reparent.
- `parent`: The identifier of the new parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentcollection/reparent(ids:to:))*