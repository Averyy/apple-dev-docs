# SeatState

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for seat data that TabletopKit syncs between players.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol SeatState
```

## Topics

### Setting the data that syncs
- [var context: UInt64](seatstate/context.md)
  An integer value that your game uses.
- [var playerID: PlayerIdentifier?](seatstate/playerid.md)
  The identifier for the player that occupies the seat.
- [var pose: TableVisualState.Pose2D](seatstate/pose.md)
  The position and orientation of the seat in table space.

## Relationships

### Conforming Types
- [TableSeatState](tableseatstate.md)

## See Also

- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/seatstate)*