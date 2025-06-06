# CardState

**Framework**: TabletopKit  
**Kind**: struct

A state for cards that contains face up and down information.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CardState
```

## Topics

### Creating a card state
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](cardstate/init(faceup:parentid:seatcontrol:pose:boundingbox:).md)
  Creates the state of a card using its visibility, location, and player interactions.
- [init(faceUp: Bool, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](cardstate/init(faceup:parentid:seatcontrol:pose:entity:).md)
  Creates a card state with the given faceUp value, parent, controlling seats, pose, and associated entity providing the bounding box.
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:boundingbox:).md)
- [static func faceDown(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](cardstate/facedown(parentid:seatcontrol:pose:entity:).md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D) -> CardState](cardstate/faceup(parentid:seatcontrol:pose:boundingbox:).md)
- [static func faceUp(parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity) -> CardState](cardstate/faceup(parentid:seatcontrol:pose:entity:).md)
### Getting the card data
- [var faceUp: Bool](cardstate/faceup.md)
  A Boolean value that indicates whether the card is oriented face up, revealing its contents.
### Getting the parent equipment
- [var parentID: EquipmentIdentifier](cardstate/parentid.md)
  The identifier for the parent equipment that holds or contains this equipment.
### Rendering the equipment
- [var boundingBox: Rect3D](cardstate/boundingbox.md)
  A 3D bounding box that encloses the card.
- [var pose: TableVisualState.Pose2D](cardstate/pose.md)
  The 2D position and rotation of the equipment relative to the equipment parent, or table.
### Controlling the equipment
- [var lockedBy: PlayerIdentifier?](cardstate/lockedby.md)
  The identifier for the player who exclusively controls the equipment.
- [var seatControl: ControllingSeats](cardstate/seatcontrol.md)
  The seats that can manipulate or interact with the equipment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [EquipmentState](equipmentstate.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/cardstate)*