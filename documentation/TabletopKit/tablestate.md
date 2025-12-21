# TableState

**Framework**: TabletopKit  
**Kind**: struct

The state of the table that can be queried and modified.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct TableState
```

## Topics

### Getting the table state
- [var counters: CounterCollection](tablestate/counters.md)
  The collection of score counters.
- [var equipment: EquipmentCollection](tablestate/equipment.md)
  The collection of equipment.
- [var turn: Set<TableSeatIdentifier>](tablestate/turn.md)
  The seats that are currently in turn.

## See Also

- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablestate)*