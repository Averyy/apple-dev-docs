# faceUp(parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity) -> CardState
```

## See Also

- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](cardstate/init(faceup:parentid:seatcontrol:pose:boundingbox:).md)
  Creates the state of a card using its visibility, location, and player interactions.
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](cardstate/init(faceup:parentid:seatcontrol:pose:entity:).md)
  Creates a card state with the given faceUp value, parent, controlling seats, pose, and associated entity providing the bounding box.
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:boundingbox:).md)
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:entity:).md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/faceup(parentid:seatcontrol:pose:boundingbox:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/cardstate/faceup(parentid:seatcontrol:pose:entity:))*