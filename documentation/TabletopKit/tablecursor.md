# TableCursor

**Framework**: TabletopKit  
**Kind**: struct

A visual indicator that represents the destination of player interactions with equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableCursor
```

## Topics

### Getting the associated interaction
- [var interactionID: TabletopInteraction.Identifier](tablecursor/interactionid.md)
  The interaction id for the cursor.
### Getting the player performing the interaction
- [var playerID: PlayerIdentifier](tablecursor/playerid.md)
  The player that the cursor represents.
### Getting information about the equipment in the interaction
- [let controlledEquipmentPose: EquipmentPose3D](tablecursor/controlledequipmentpose.md)
  Pose relative to the the table
- [var hovering: TabletopInteraction.Destination?](tablecursor/hovering.md)
  The cursor’s current position, relative to the table or a piece of equipment.
### Getting the cursor identifier
- [var id: TableCursor.ID](tablecursor/id.md)
  The interaction identifier for the cursor.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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