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
### Instance Methods
- [func bounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(for:).md)
  Returns the current pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func goalBounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(for:).md)
  Returns the goal pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func goalPose(for: some Equipment) -> Pose3D?](tablevisualstate/goalpose(for:).md)
  Returns the goal pose for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func goalPose(matching: EquipmentIdentifier) -> Pose3D?](tablevisualstate/goalpose(matching:).md)
  Returns the goal pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.
- [func pose(for: some Equipment) -> Pose3D?](tablevisualstate/pose(for:)-50h4r.md)
  Returns the current pose for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func pose(for: some TableSeat) -> Pose3D?](tablevisualstate/pose(for:)-8pm0h.md)
  Returns the pose for the given seat. Returns `nil` if the seat is not part of the game.
- [func pose(matching: TableSeatIdentifier) -> Pose3D?](tablevisualstate/pose(matching:)-6bo29.md)
- [func pose(matching: EquipmentIdentifier) -> Pose3D?](tablevisualstate/pose(matching:)-8nqm2.md)
  Returns the current pose for the equipment matching the given ID. Returns `nil` if the equipment is not part of the game.

## See Also

- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate)*