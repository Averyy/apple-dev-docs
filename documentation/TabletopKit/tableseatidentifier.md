# TableSeatIdentifier

**Framework**: TabletopKit  
**Kind**: struct

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
- [init(Int)](tableseatidentifier/init(_:).md)
### Getting identifier values
- [let rawValue: Int](tableseatidentifier/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tableseatidentifier)*