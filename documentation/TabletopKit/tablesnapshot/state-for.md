# state(for:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func state<E>(for equipment: E) -> E.State where E : Equipment
```

## See Also

- [var turn: Set<TableSeatIdentifier>](tablesnapshot/turn.md)
- [var seats: [any TableSeat]](tablesnapshot/seats.md)
- [var seatIDs: [TableSeatIdentifier]](tablesnapshot/seatids.md)
- [func seat<S>(of: S.Type, for: Player) -> (S, S.State)?](tablesnapshot/seat(of:for:).md)
- [func seat<S>(of: S.Type, matching: TableSeatIdentifier) -> (S, S.State)?](tablesnapshot/seat(of:matching:).md)
- [func seats<S>(of: S.Type) -> [(S, S.State)]](tablesnapshot/seats(of:).md)
- [func state(matching: TableSeatIdentifier) -> (any SeatState)?](tablesnapshot/state(matching:)-ear2.md)
- [func entity(forSeat: some EntityTableSeat) -> Entity?](tablesnapshot/entity(forseat:).md)
- [func entity(matching: TableSeatIdentifier) -> Entity?](tablesnapshot/entity(matching:)-7ps7s.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/state(for:))*