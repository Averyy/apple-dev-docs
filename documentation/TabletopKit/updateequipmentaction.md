# UpdateEquipmentAction

**Framework**: TabletopKit  
**Kind**: struct

An action that updates properties of equipment on the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct UpdateEquipmentAction<State> where State : EquipmentState
```

#### Overview

To create an update equipment action, use the [`updateEquipment(_:state:context:)`](tabletopaction/updateequipment(_:state:context:)-6kawf.md) or a similar static method.

## Topics

### Getting the equipment in the action
- [var equipmentID: EquipmentIdentifier](updateequipmentaction/equipmentid.md)
  The ID of the equipment to update.
### Getting the state of the equipment
- [var newState: State?](updateequipmentaction/newstate.md)
  The new state of the equipment.
### Instance Properties
- [var context: UInt64](updateequipmentaction/context.md)
  An integer value that your game uses.
- [var playerID: Player.ID?](updateequipmentaction/playerid.md)
  The player performing the action.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [TabletopAction](tabletopaction.md)

## See Also

- [protocol TabletopAction](tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct MoveEquipmentAction](moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct SetTurnAction](setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct UpdateCounterAction](updatecounteraction.md)
  An action that updates the game counter.
- [struct CreateBookmarkAction](createbookmarkaction.md)
  An action that takes a snapshot of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/updateequipmentaction)*