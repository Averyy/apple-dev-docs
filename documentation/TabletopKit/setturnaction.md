# SetTurnAction

**Framework**: TabletopKit  
**Kind**: struct

An action that sets the current seats participating in the current turn.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SetTurnAction
```

#### Overview

To create a set turn action, use the [`setTurn(forSeat:context:)`](tabletopaction/setturn(forseat:context:).md) or a similar static method.

## Topics

### Getting the seats involved in a turn
- [var seatIDsInTurn: [TableSeatIdentifier]](setturnaction/seatidsinturn.md)
  The IDs of the seats that are part of the current turn.
### Instance Properties
- [var context: UInt64](setturnaction/context.md)
  An integer value that your game uses.
- [var playerID: Player.ID?](setturnaction/playerid.md)
  The ID of the player who is setting the turn.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabletopAction](tabletopaction.md)

## See Also

- [protocol TabletopAction](tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct MoveEquipmentAction](moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct UpdateEquipmentAction](updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct UpdateCounterAction](updatecounteraction.md)
  An action that updates the game counter.
- [struct CreateBookmarkAction](createbookmarkaction.md)
  An action that takes a snapshot of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/setturnaction)*