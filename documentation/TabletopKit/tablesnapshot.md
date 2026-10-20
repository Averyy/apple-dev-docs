# TableSnapshot

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A snapshot of the current state of the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableSnapshot
```

## Topics

### Getting the table entity
- [var tableEntity: Entity?](./tablesnapshot/tableentity.md)
### Getting information on seats
- [var turn: Set<TableSeatIdentifier>](./tablesnapshot/turn.md)
- [var seats: [any TableSeat]](./tablesnapshot/seats.md)
- [var seatIDs: [TableSeatIdentifier]](./tablesnapshot/seatids.md)
- [func seat<S>(of: S.Type, for: Player) -> (S, S.State)?](./tablesnapshot/seat%28of,for%29.md)
- [func seat<S>(of: S.Type, matching: TableSeatIdentifier) -> (S, S.State)?](./tablesnapshot/seat%28of,matching%29.md)
- [func seats<S>(of: S.Type) -> [(S, S.State)]](./tablesnapshot/seats%28of%29.md)
- [func state<E>(for: E) -> E.State](./tablesnapshot/state%28for%29.md)
- [func state(matching: TableSeatIdentifier) -> (any SeatState)?](./tablesnapshot/state%28matching%29-ear2.md)
- [func entity(forSeat: some EntityTableSeat) -> Entity?](./tablesnapshot/entity%28forseat%29.md)
- [func entity(matching: TableSeatIdentifier) -> Entity?](./tablesnapshot/entity%28matching%29-7ps7s.md)
### Getting cursors
- [var cursors: [TableCursor]](./tablesnapshot/cursors.md)
- [func cursor(matching: TableCursorIdentifier) -> TableCursor?](./tablesnapshot/cursor%28matching%29.md)
- [func cursor(controlling: EquipmentIdentifier) -> TableCursor?](./tablesnapshot/cursor%28controlling%29.md)
  Returns the cursor corresponding to an interaction controlling the given equipment ID, or `nil` if no such cursors could be found.
- [func cursors(forPlayer: Player) -> [TableCursor]](./tablesnapshot/cursors%28forplayer%29.md)
- [func cursors(hovering: EquipmentIdentifier) -> [TableCursor]](./tablesnapshot/cursors%28hovering%29.md)
- [func cursors(controlling: some Sequence<EquipmentIdentifier>) -> [TableCursor]](./tablesnapshot/cursors%28controlling%29.md)
  Finds and returns all the cursors corresponding to an interactions controlling any of the given equipment IDs. Duplicate equipment IDs are ignored.
- [func cursors(for: Player) -> [TableCursor]](./tablesnapshot/cursors%28for%29.md)
  Finds and returns all the cursors corresponding to an interactions owned by the given player.
- [func cursors(matching: TabletopInteraction.Identifier) -> [TableCursor]](./tablesnapshot/cursors%28matching%29.md)
  Finds and returns all the cursors corresponding to a given interaction.
### Getting information on equipment
- [func equipment<E>(of: E.Type) -> [(E, E.State)]](./tablesnapshot/equipment%28of%29.md)
- [func equipment<E>(of: E.Type, childrenOf: some Equipment) -> [(E, E.State)]](./tablesnapshot/equipment%28of,childrenof%29-4z4s1.md)
- [func equipment<E>(of: E.Type, childrenOf: EquipmentIdentifier) -> [(E, E.State)]](./tablesnapshot/equipment%28of,childrenof%29-5w137.md)
- [func equipment<E>(of: E.Type, matching: some Sequence<EquipmentIdentifier>) -> [(E, E.State)]](./tablesnapshot/equipment%28of,matching%29-7ai0c.md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> (E, E.State)?](./tablesnapshot/equipment%28of,matching%29-8qve2.md)
- [func equipmentIDs() -> [EquipmentIdentifier]](./tablesnapshot/equipmentids%28%29.md)
- [func equipmentIDs(childrenOf: some Equipment) -> [EquipmentIdentifier]](./tablesnapshot/equipmentids%28childrenof%29-432sk.md)
- [func equipmentIDs(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](./tablesnapshot/equipmentids%28childrenof%29-f1sp.md)
- [func state(matching: EquipmentIdentifier) -> (any EquipmentState)?](./tablesnapshot/state%28matching%29-u35k.md)
- [func entity(matching: EquipmentIdentifier) -> Entity?](./tablesnapshot/entity%28matching%29-vb9w.md)
- [func entity(forEquipment: some EntityEquipment) -> Entity?](./tablesnapshot/entity%28forequipment%29.md)
### Getting score counters
- [var counters: [ScoreCounter]](./tablesnapshot/counters.md)
- [func counter(matching: ScoreCounter.ID) -> ScoreCounter?](./tablesnapshot/counter%28matching%29.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Escapable](../Swift/escapable.md)

## See Also

### Interactions
- [Simulating dice rolls as a component for your game](./simulating-dice-rolls-as-a-component-for-your-game.md)
  Create a physically realistic dice game by adding interactive rolling and scoring.
- [class TabletopInteraction](./tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](./tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableVisualState](./tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](./tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](./tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot)*