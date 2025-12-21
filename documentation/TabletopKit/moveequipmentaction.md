# MoveEquipmentAction

**Framework**: TabletopKit  
**Kind**: struct

An action that moves a piece of equipment on the table or changes the grouping.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct MoveEquipmentAction
```

#### Overview

To create a move equipment action, use the [`moveEquipment(_:childOf:order:pose:context:)`](tabletopaction/moveequipment(_:childof:order:pose:context:).md) or the [`moveEquipment(matching:childOf:order:pose:context:)`](tabletopaction/moveequipment(matching:childof:order:pose:context:).md) static method.

## Topics

### Getting the equipment in the action
- [var equipmentID: EquipmentIdentifier](moveequipmentaction/equipmentid.md)
  The ID of the equipment being moved.
- [var parentID: EquipmentIdentifier](moveequipmentaction/parentid.md)
  The equipment ID the moved equipment is being grouped under
- [var playerID: Player.ID?](moveequipmentaction/playerid.md)
  The ID of the player who is moving the equipment.
- [var order: MoveEquipmentAction.Order?](moveequipmentaction/order-swift.property.md)
  The order in which the equipment should be inserted.
- [MoveEquipmentAction.Order](moveequipmentaction/order-swift.enum.md)
  The possible orders of equipment.
### Getting the position of the equipment
- [var pose: TableVisualState.Pose2D?](moveequipmentaction/pose.md)
  The position the equipment being moved to
### Getting game-specific information
- [var context: UInt64](moveequipmentaction/context.md)
  An integer value that your game uses.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabletopAction](tabletopaction.md)

## See Also

- [protocol TabletopAction](tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct UpdateEquipmentAction](updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct SetTurnAction](setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct UpdateCounterAction](updatecounteraction.md)
  An action that updates the game counter.
- [struct CreateBookmarkAction](createbookmarkaction.md)
  An action that takes a snapshot of the game.
- [protocol CustomAction](customaction.md)
  A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/moveequipmentaction)*