# pose(forSeat:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+ - Deprecated in 26.0 (renamed: pose(for:))

## Declaration

```swift
func pose(forSeat seat: some TableSeat) -> Pose3D?
```

## See Also

### Representing seat states
- [func pose(for: some Equipment) -> Pose3D?](./pose%28for%29-50h4r.md)
  Returns the current pose for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func pose(for: some TableSeat) -> Pose3D?](./pose%28for%29-8pm0h.md)
  Returns the pose for the given seat. Returns `nil` if the seat is not part of the game.
- [func pose(matching: TableSeatIdentifier) -> Pose3D?](./pose%28matching%29-6bo29.md)
- [func pose(matching: EquipmentIdentifier) -> Pose3D?](./pose%28matching%29-8nqm2.md)
  Returns the current pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/pose(forseat:))*