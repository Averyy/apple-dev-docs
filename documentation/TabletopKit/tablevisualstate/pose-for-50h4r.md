# pose(for:)

**Framework**: TabletopKit  
**Kind**: method

Returns the current pose for the given equipment. Returns `nil` if the equipment is not part of the game.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func pose(for equipment: some Equipment) -> Pose3D?
```

## See Also

- [func pose(for: some TableSeat) -> Pose3D?](tablevisualstate/pose(for:)-8pm0h.md)
  Returns the pose for the given seat. Returns `nil` if the seat is not part of the game.
- [func pose(forSeat: some TableSeat) -> Pose3D?](tablevisualstate/pose(forseat:).md)
- [func pose(matching: TableSeatIdentifier) -> Pose3D?](tablevisualstate/pose(matching:)-6bo29.md)
- [func pose(matching: EquipmentIdentifier) -> Pose3D?](tablevisualstate/pose(matching:)-8nqm2.md)
  Returns the current pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/pose(for:)-50h4r)*