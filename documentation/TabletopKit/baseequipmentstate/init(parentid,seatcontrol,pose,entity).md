# init(parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency init(parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity)
```

## See Also

### Creating an equipment state
- [init(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](./init%28parentid,seatcontrol,pose,boundingbox%29.md)
  Creates a base state for equipment using a parent, location, and player interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/baseequipmentstate/init(parentid:seatcontrol:pose:entity:))*