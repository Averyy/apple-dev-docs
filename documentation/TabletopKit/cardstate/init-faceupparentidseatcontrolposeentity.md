# init(faceUp:parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: init

Creates a card state with the given faceUp value, parent, controlling seats, pose, and associated entity providing the bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity)
```

## See Also

- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](cardstate/init(faceup:parentid:seatcontrol:pose:boundingbox:).md)
  Creates the state of a card using its visibility, location, and player interactions.
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:boundingbox:).md)
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:entity:).md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/faceup(parentid:seatcontrol:pose:boundingbox:).md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](cardstate/faceup(parentid:seatcontrol:pose:entity:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/cardstate/init(faceup:parentid:seatcontrol:pose:entity:))*