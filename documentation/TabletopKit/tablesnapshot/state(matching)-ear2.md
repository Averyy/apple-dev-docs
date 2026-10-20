# state(matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func state(matching seatID: TableSeatIdentifier) -> (any SeatState)?
```

## See Also

### Getting information on seats
- [var turn: Set<TableSeatIdentifier>](./turn.md)
- [var seats: [any TableSeat]](./seats.md)
- [var seatIDs: [TableSeatIdentifier]](./seatids.md)
- [func seat<S>(of: S.Type, for: Player) -> (S, S.State)?](./seat%28of,for%29.md)
- [func seat<S>(of: S.Type, matching: TableSeatIdentifier) -> (S, S.State)?](./seat%28of,matching%29.md)
- [func seats<S>(of: S.Type) -> [(S, S.State)]](./seats%28of%29.md)
- [func state<E>(for: E) -> E.State](./state%28for%29.md)
- [func entity(forSeat: some EntityTableSeat) -> Entity?](./entity%28forseat%29.md)
- [func entity(matching: TableSeatIdentifier) -> Entity?](./entity%28matching%29-7ps7s.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/state(matching:)-ear2)*