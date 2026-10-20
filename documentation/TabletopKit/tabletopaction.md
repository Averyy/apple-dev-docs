# TabletopAction

**Framework**: TabletopKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for objects that describe an action in a tabletop game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol TabletopAction
```

## Topics

### Getting the player
- [var playerID: PlayerIdentifier?](./tabletopaction/playerid.md)
  The player performing the action.
### Getting game-specific information
- [var context: UInt64](./tabletopaction/context.md)
  An integer value that your game uses.
### Moving equipment
- [static func moveEquipment(some Equipment, childOf: any Equipment, order: MoveEquipmentAction.Order?, pose: TableVisualState.Pose2D?, context: UInt64) -> Self](./tabletopaction/moveequipment%28_,childof,order,pose,context%29.md)
- [static func moveEquipment(matching: EquipmentIdentifier, childOf: EquipmentIdentifier, order: MoveEquipmentAction.Order?, pose: TableVisualState.Pose2D?, context: UInt64) -> Self](./tabletopaction/moveequipment%28matching,childof,order,pose,context%29.md)
### Changing equipment state properties
- [static func updateEquipment<E>(E, faceUp: Bool?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,faceup,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, rawValue: UInt64?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,rawvalue,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,state,context%29-6kawf.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,state,context%29-88v3m.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,state,context%29-8tmnn.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,state,context%29-j62v.md)
- [static func updateEquipment<E>(E, value: Int?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./tabletopaction/updateequipment%28_,value,seatcontrol,pose,boundingbox,context%29.md)
### Taking turns
- [static func setTurn(forSeat: some TableSeat, context: UInt64) -> Self](./tabletopaction/setturn%28forseat,context%29.md)
- [static func setTurn(forSeats: some Sequence, context: UInt64) -> Self](./tabletopaction/setturn%28forseats,context%29-3msxi.md)
- [static func setTurn(forSeats: some Sequence<any TableSeat>, context: UInt64) -> Self](./tabletopaction/setturn%28forseats,context%29-4sgng.md)
- [static func setTurn(matching: TableSeatIdentifier, context: UInt64) -> Self](./tabletopaction/setturn%28matching,context%29-6mq07.md)
- [static func setTurn(matching: [TableSeatIdentifier], context: UInt64) -> Self](./tabletopaction/setturn%28matching,context%29-88ymv.md)
### Keeping score
- [static func updateCounter(ScoreCounter, context: UInt64) -> Self](./tabletopaction/updatecounter%28_,context%29.md)
- [static func updateCounter(matching: ScoreCounter.Identifier, value: Int64, context: UInt64) -> Self](./tabletopaction/updatecounter%28matching,value,context%29.md)
### Creating bookmarks
- [static func createBookmark(StateBookmark, context: UInt64) -> Self](./tabletopaction/createbookmark%28_,context%29.md)
- [static func createBookmark(id: StateBookmarkIdentifier, context: UInt64) -> Self](./tabletopaction/createbookmark%28id,context%29.md)
### Adding actions
- [static func customAction(some CustomAction, context: UInt64) -> Self](./tabletopaction/customaction%28_,context%29.md)

## Relationships

### Conforming Types
- [CreateBookmarkAction](./createbookmarkaction.md)
- [MoveEquipmentAction](./moveequipmentaction.md)
- [SetTurnAction](./setturnaction.md)
- [UpdateCounterAction](./updatecounteraction.md)
- [UpdateEquipmentAction](./updateequipmentaction.md)

## See Also

### Actions
- [struct MoveEquipmentAction](./moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct UpdateEquipmentAction](./updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct SetTurnAction](./setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct UpdateCounterAction](./updatecounteraction.md)
  An action that updates the game counter.
- [struct CreateBookmarkAction](./createbookmarkaction.md)
  An action that takes a snapshot of the game.
- [protocol CustomAction](./customaction.md)
  A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction)*