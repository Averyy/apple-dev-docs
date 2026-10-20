# tableBounds

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var tableBounds: TableVisualState.OrientedRect3D? { get }
```

## See Also

### Representing 3D states
- [TableVisualState.OrientedRect3D](./orientedrect3d.md)
  An object that represents the position and orientation of a 3D rectangle.
- [func bounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](./bounds%28for%29.md)
  Returns the current pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func bounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](./bounds%28forequipment%29.md)
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./bounds%28matching%29.md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](./goalbounds%28forequipment%29.md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./goalbounds%28matching%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/tablebounds)*