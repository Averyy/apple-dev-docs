# pose(matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Returns the current pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func pose(matching equipmentID: EquipmentIdentifier) -> Pose3D?
```

## See Also

### Representing seat states
- [func pose(for: some Equipment) -> Pose3D?](./pose%28for%29-50h4r.md)
  Returns the current pose for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func pose(for: some TableSeat) -> Pose3D?](./pose%28for%29-8pm0h.md)
  Returns the pose for the given seat. Returns `nil` if the seat is not part of the game.
- [func pose(forSeat: some TableSeat) -> Pose3D?](./pose%28forseat%29.md)
- [func pose(matching: TableSeatIdentifier) -> Pose3D?](./pose%28matching%29-6bo29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/pose(matching:)-8nqm2)*