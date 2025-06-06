# init(value:parentID:seatControl:pose:boundingBox:)

**Framework**: TabletopKit  
**Kind**: init

Creates the state of a die using the specified current value, location, and player interactions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, boundingBox: Rect3D)
```

## See Also

- [init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](diestate/init(value:parentid:seatcontrol:pose:entity:).md)
  Creates a die state with the given die value, parent, controlling seats, pose, and associated entity providing the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/diestate/init(value:parentid:seatcontrol:pose:boundingbox:))*