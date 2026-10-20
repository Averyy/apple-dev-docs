# TableSeatIdentifier

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A unique identifier for seats.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableSeatIdentifier
```

#### Overview

The seat identifier needs to be unique across all instances of the same tabletop game.

## Topics

### Creating seat identifiers
- [init(Int)](./tableseatidentifier/init%28_%29.md)
### Getting identifier values
- [let rawValue: Int](./tableseatidentifier/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Seats
- [struct TableState](./tablestate.md)
  The state of the table that can be queried and modified.
- [protocol TableSeat](./tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](./entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatState](./tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](./seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tableseatidentifier)*