# init(faceUp:parentID:seatControl:pose:boundingBox:)

**Framework**: TabletopKit  
**Kind**: init  
**Role**: Initializer

Creates the state of a card using its visibility, location, and player interactions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, boundingBox: Rect3D)
```

## See Also

### Creating a card state
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](./init%28faceup,parentid,seatcontrol,pose,entity%29.md)
  Creates a card state with the given faceUp value, parent, controlling seats, pose, and associated entity providing the bounding box.
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](./facedown%28parentid,seatcontrol,pose,boundingbox%29.md)
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](./facedown%28parentid,seatcontrol,pose,entity%29.md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](./faceup%28parentid,seatcontrol,pose,boundingbox%29.md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](./faceup%28parentid,seatcontrol,pose,entity%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/cardstate/init(faceup:parentid:seatcontrol:pose:boundingbox:))*