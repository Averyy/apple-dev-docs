# init(value:parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: init  
**Role**: Initializer

Creates a die state with the given die value, parent, controlling seats, pose, and associated entity providing the bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity)
```

## See Also

### Creating a die state
- [init(value: Int, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](./init%28value,parentid,seatcontrol,pose,boundingbox%29.md)
  Creates the state of a die using the specified current value, location, and player interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/diestate/init(value:parentid:seatcontrol:pose:entity:))*