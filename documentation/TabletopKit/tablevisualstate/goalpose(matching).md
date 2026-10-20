# goalPose(matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Returns the goal pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func goalPose(matching equipmentID: EquipmentIdentifier) -> Pose3D?
```

## See Also

### Representing the goal
- [func goalBounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](./goalbounds%28for%29.md)
  Returns the goal pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func goalPose(for: some Equipment) -> Pose3D?](./goalpose%28for%29.md)
  Returns the goal pose for the given equipment. Returns `nil` if the equipment is not part of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/goalpose(matching:))*