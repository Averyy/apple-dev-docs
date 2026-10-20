# faceDown(parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity) -> CardState
```

## See Also

### Creating a card state
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](./init%28faceup,parentid,seatcontrol,pose,boundingbox%29.md)
  Creates the state of a card using its visibility, location, and player interactions.
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](./init%28faceup,parentid,seatcontrol,pose,entity%29.md)
  Creates a card state with the given faceUp value, parent, controlling seats, pose, and associated entity providing the bounding box.
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](./facedown%28parentid,seatcontrol,pose,boundingbox%29.md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](./faceup%28parentid,seatcontrol,pose,boundingbox%29.md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](./faceup%28parentid,seatcontrol,pose,entity%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/cardstate/facedown(parentid:seatcontrol:pose:entity:))*