# init(value:parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: init

Creates a die state with the given die value, parent, controlling seats, pose, and associated entity providing the bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity)
```

## See Also

- [init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](diestate/init(value:parentid:seatcontrol:pose:boundingbox:).md)
  Creates the state of a die using the specified current value, location, and player interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/diestate/init(value:parentid:seatcontrol:pose:entity:))*