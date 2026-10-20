# init(parentID:seatControl:pose:boundingBox:)

**Framework**: TabletopKit  
**Kind**: init  
**Role**: Initializer

Creates a base state for equipment using a parent, location, and player interactions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, boundingBox: Rect3D = .init())
```

## See Also

### Creating an equipment state
- [init(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](./init%28parentid,seatcontrol,pose,entity%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/baseequipmentstate/init(parentid:seatcontrol:pose:boundingbox:))*