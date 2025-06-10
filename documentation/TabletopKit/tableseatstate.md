# TableSeatState

**Framework**: TabletopKit  
**Kind**: struct

The data associated with a seat that a player occupies.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableSeatState
```

## Topics

### Creating a seat state structure
- [init(pose: TableVisualState.Pose2D, context: UInt64)](tableseatstate/init(pose:context:).md)
  Creates the state of a seat using the specified pose and optional, game-specific data.
### Setting the data that syncs
- [var playerID: Player.ID?](tableseatstate/playerid.md)
  The identifier for the player who occupies the seat.
- [var pose: TableVisualState.Pose2D](tableseatstate/pose.md)
  The position and orientation of the seat around the table.

## Relationships

### Conforms To
- [SeatState](seatstate.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tableseatstate)*