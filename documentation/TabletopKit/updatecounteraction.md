# UpdateCounterAction

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An action that updates the game counter.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct UpdateCounterAction
```

#### Overview

To create an update counter action, use the [`updateCounter(_:context:)`](./tabletopaction/updatecounter%28_,context%29.md) or the [`updateCounter(matching:value:context:)`](./tabletopaction/updatecounter%28matching,value,context%29.md) static method.

## Topics

### Getting counter information
- [var counterID: ScoreCounter.Identifier](./updatecounteraction/counterid.md)
  The ID of the counter to update.
- [var newValue: Int64](./updatecounteraction/newvalue.md)
  The new value to set for the counter.
### Getting game-specific information
- [var context: UInt64](./updatecounteraction/context.md)
  An integer value that your game uses.
### Getting the player identifier
- [var playerID: Player.ID?](./updatecounteraction/playerid.md)
  The ID of the player who is updating the counter.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TabletopAction](./tabletopaction.md)

## See Also

### Actions
- [protocol TabletopAction](./tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct MoveEquipmentAction](./moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct UpdateEquipmentAction](./updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct SetTurnAction](./setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct CreateBookmarkAction](./createbookmarkaction.md)
  An action that takes a snapshot of the game.
- [protocol CustomAction](./customaction.md)
  A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/updatecounteraction)*