# bounds(forEquipment:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+ - Deprecated in 26.0 (renamed: bounds(for:))

## Declaration

```swift
func bounds(forEquipment equipment: some Equipment) -> TableVisualState.OrientedRect3D?
```

## See Also

### Representing 3D states
- [TableVisualState.OrientedRect3D](./orientedrect3d.md)
  An object that represents the position and orientation of a 3D rectangle.
- [func bounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](./bounds%28for%29.md)
  Returns the current pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./bounds%28matching%29.md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](./goalbounds%28forequipment%29.md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./goalbounds%28matching%29.md)
- [var tableBounds: TableVisualState.OrientedRect3D?](./tablebounds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/bounds(forequipment:))*