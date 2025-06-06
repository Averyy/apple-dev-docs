# EntityTableSeat

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for seats at the table that you render using RealityKit.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EntityTableSeat : TableSeat
```

#### Overview

To render seats using an entity, follow these steps:

1. Create a structure that conforms to this protocol.
2. Set the [`State`](tableseat/state.md) type alias to [`TableSeatState`](tableseatstate.md).
3. Declare the `id` property as a [`TableSeatIdentifier`](tableseatidentifier.md) structure.
4. Declare the [`initialState`](tableseat/initialstate.md) property as a [`State`](tableseat/state.md) structure.
5. Implement an initializer that sets these properties and the [`entity`](entitytableseat/entity.md) property.

## Topics

### Rendering the equipment
- [var entity: Entity](entitytableseat/entity.md)
  The entity associated with the seat.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
- [TableSeat](tableseat.md)

## See Also

- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/entitytableseat)*