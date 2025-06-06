# TableVisualState

**Framework**: TabletopKit  
**Kind**: struct

A structure that represents the appearance of an object on the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableVisualState
```

## Topics

### Representing collision states
- [var contacts: some Sequence<TableVisualState.Contact>](tablevisualstate/contacts.md)
  Returns all contacts for the current update of the physics simulation.
- [func contacts<E>(of: E.Type) -> some Sequence<TableVisualState.Contact>
](tablevisualstate/contacts(of:).md)
  Returns all contacts for the current update of the physics simulation for a specified equipment type.
- [TableVisualState.Contact](tablevisualstate/contact.md)
  An object that represents the contact of a collision during a simulation of tossable equipment.
### Representing 2D states
- [TableVisualState.Point2D](tablevisualstate/point2d.md)
  An object that represents a point on the XZ plane.
- [TableVisualState.Pose2D](tablevisualstate/pose2d.md)
  An object that represents a 2D position and orientation on the XZ plane.
### Representing 3D states
- [TableVisualState.OrientedRect3D](tablevisualstate/orientedrect3d.md)
  An object that represents the position and orientation of a 3D rectangle.
- [func bounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(forequipment:).md)
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(matching:).md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(forequipment:).md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(matching:).md)
- [var tableBounds: TableVisualState.OrientedRect3D?](tablevisualstate/tablebounds.md)
### Representing seat states
- [func pose(forSeat: some TableSeat) -> Pose3D?](tablevisualstate/pose(forseat:).md)
- [func pose(matching: TableSeatIdentifier) -> Pose3D?](tablevisualstate/pose(matching:).md)

## See Also

- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableCursor](tablecursor.md)
  A visual indicator that represents the destination of player interactions with equipment.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate)*