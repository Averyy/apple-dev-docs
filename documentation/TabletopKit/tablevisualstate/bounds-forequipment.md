# bounds(forEquipment:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func bounds(forEquipment equipment: some Equipment) -> TableVisualState.OrientedRect3D?
```

## See Also

- [TableVisualState.OrientedRect3D](tablevisualstate/orientedrect3d.md)
  An object that represents the position and orientation of a 3D rectangle.
- [func bounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(for:).md)
  Returns the current pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(matching:).md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(forequipment:).md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(matching:).md)
- [var tableBounds: TableVisualState.OrientedRect3D?](tablevisualstate/tablebounds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/bounds(forequipment:))*