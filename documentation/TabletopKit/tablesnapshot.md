# TableSnapshot

**Framework**: TabletopKit  
**Kind**: struct

A snapshot of the current state of the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableSnapshot
```

## Topics

### Getting the table entity
- [var tableEntity: Entity?](tablesnapshot/tableentity.md)
### Getting information on seats
- [var turn: Set<TableSeatIdentifier>](tablesnapshot/turn.md)
- [var seats: [any TableSeat]](tablesnapshot/seats.md)
- [var seatIDs: [TableSeatIdentifier]](tablesnapshot/seatids.md)
- [func seat<S>(of: S.Type, for: Player) -> (S, S.State)?](tablesnapshot/seat(of:for:).md)
- [func seat<S>(of: S.Type, matching: TableSeatIdentifier) -> (S, S.State)?](tablesnapshot/seat(of:matching:).md)
- [func seats<S>(of: S.Type) -> [(S, S.State)]](tablesnapshot/seats(of:).md)
- [func state<E>(for: E) -> E.State](tablesnapshot/state(for:).md)
- [func state(matching: TableSeatIdentifier) -> (any SeatState)?](tablesnapshot/state(matching:)-ear2.md)
- [func entity(forSeat: some EntityTableSeat) -> Entity?](tablesnapshot/entity(forseat:).md)
- [func entity(matching: TableSeatIdentifier) -> Entity?](tablesnapshot/entity(matching:)-7ps7s.md)
### Getting cursors
- [var cursors: [TableCursor]](tablesnapshot/cursors.md)
- [func cursor(matching: TableCursorIdentifier) -> TableCursor?](tablesnapshot/cursor(matching:).md)
- [func cursor(controlling: EquipmentIdentifier) -> TableCursor?](tablesnapshot/cursor(controlling:).md)
  Returns the cursor corresponding to an interaction controlling the given equipment ID, or `nil` if no such cursors could be found.
- [func cursors(forPlayer: Player) -> [TableCursor]](tablesnapshot/cursors(forplayer:).md)
- [func cursors(hovering: EquipmentIdentifier) -> [TableCursor]](tablesnapshot/cursors(hovering:).md)
- [func cursors(controlling: some Sequence<EquipmentIdentifier>) -> [TableCursor]](tablesnapshot/cursors(controlling:).md)
  Finds and returns all the cursors corresponding to an interactions controlling any of the given equipment IDs. Duplicate equipment IDs are ignored.
- [func cursors(for: Player) -> [TableCursor]](tablesnapshot/cursors(for:).md)
  Finds and returns all the cursors corresponding to an interactions owned by the given player.
- [func cursors(matching: TabletopInteraction.Identifier) -> [TableCursor]](tablesnapshot/cursors(matching:).md)
  Finds and returns all the cursors corresponding to a given interaction.
### Getting information on equipment
- [func equipment<E>(of: E.Type) -> [(E, E.State)]](tablesnapshot/equipment(of:).md)
- [func equipment<E>(of: E.Type, childrenOf: some Equipment) -> [(E, E.State)]](tablesnapshot/equipment(of:childrenof:)-4z4s1.md)
- [func equipment<E>(of: E.Type, childrenOf: EquipmentIdentifier) -> [(E, E.State)]](tablesnapshot/equipment(of:childrenof:)-5w137.md)
- [func equipment<E>(of: E.Type, matching: some Sequence<EquipmentIdentifier>) -> [(E, E.State)]](tablesnapshot/equipment(of:matching:)-7ai0c.md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> (E, E.State)?](tablesnapshot/equipment(of:matching:)-8qve2.md)
- [func equipmentIDs() -> [EquipmentIdentifier]](tablesnapshot/equipmentids.md)
- [func equipmentIDs(childrenOf: some Equipment) -> [EquipmentIdentifier]](tablesnapshot/equipmentids(childrenof:)-432sk.md)
- [func equipmentIDs(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](tablesnapshot/equipmentids(childrenof:)-f1sp.md)
- [func state(matching: EquipmentIdentifier) -> (any EquipmentState)?](tablesnapshot/state(matching:)-u35k.md)
- [func entity(matching: EquipmentIdentifier) -> Entity?](tablesnapshot/entity(matching:)-vb9w.md)
- [func entity(forEquipment: some EntityEquipment) -> Entity?](tablesnapshot/entity(forequipment:).md)
### Getting score counters
- [var counters: [ScoreCounter]](tablesnapshot/counters.md)
- [func counter(matching: ScoreCounter.ID) -> ScoreCounter?](tablesnapshot/counter(matching:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)

## See Also

- [Simulating dice rolls as a component for your game](simulating-dice-rolls-as-a-component-for-your-game.md)
  Create a physically realistic dice game by adding interactive rolling and scoring.
- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot)*