# goalBounds(for:)

**Framework**: TabletopKit  
**Kind**: method

Returns the goal pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func goalBounds(for equipment: some Equipment) -> TableVisualState.OrientedRect3D?
```

## See Also

- [func goalPose(for: some Equipment) -> Pose3D?](tablevisualstate/goalpose(for:).md)
  Returns the goal pose for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func goalPose(matching: EquipmentIdentifier) -> Pose3D?](tablevisualstate/goalpose(matching:).md)
  Returns the goal pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/goalbounds(for:))*