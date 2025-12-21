# TableCursor

**Framework**: TabletopKit  
**Kind**: struct

A cursor conveys information about one equipment that is currently being controlled by an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableCursor
```

## Topics

### Getting the associated interaction
- [var interactionID: TabletopInteraction.Identifier](tablecursor/interactionid.md)
  The identifier of the interaction manipulating the equipment corresponding to this cursor.
### Getting the player performing the interaction
- [var playerID: PlayerIdentifier](tablecursor/playerid.md)
  The player that owns the interaction.
### Getting information about the equipment in the interaction
- [let controlledEquipmentPose: EquipmentPose3D](tablecursor/controlledequipmentpose.md)
  The identifier of the equipment and the pose of the equipment in table space. NOTE: the equipment pose returned here does not include the resting orientation, similarly to the `pose` and `initialPose`in `TabletopInteraction.Value`. This is unlike the `pose` returned in `TableVisualState`, which does include resting orientation.
- [var hovering: TabletopInteraction.Destination?](tablecursor/hovering.md)
  The current destination for the equipment, if the interaction were to end now. `nil` if no destination is currently available.
### Getting the cursor identifier
- [var id: TableCursor.ID](tablecursor/id.md)
  The identifier of the cursor.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Simulating dice rolls as a component for your game](simulating-dice-rolls-as-a-component-for-your-game.md)
  Create a physically realistic dice game by adding interactive rolling and scoring.
- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablecursor)*