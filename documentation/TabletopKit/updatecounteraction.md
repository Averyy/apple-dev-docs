# UpdateCounterAction

**Framework**: TabletopKit  
**Kind**: struct

An action that updates the game counter.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct UpdateCounterAction
```

#### Overview

To create an update counter action, use the [`updateCounter(_:context:)`](tabletopaction/updatecounter(_:context:).md) or the [`updateCounter(matching:value:context:)`](tabletopaction/updatecounter(matching:value:context:).md) static method.

## Topics

### Getting counter information
- [var counterID: ScoreCounter.Identifier](updatecounteraction/counterid.md)
  The ID of the counter to update.
- [var newValue: Int64](updatecounteraction/newvalue.md)
  The new value to set for the counter.
### Getting game-specific information
- [var context: UInt64](updatecounteraction/context.md)
  An integer value that your game uses.
### Instance Properties
- [var playerID: Player.ID?](updatecounteraction/playerid.md)
  The ID of the player who is updating the counter.

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
- [struct SetTurnAction](setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct CreateBookmarkAction](createbookmarkaction.md)
  An action that takes a snapshot of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/updatecounteraction)*