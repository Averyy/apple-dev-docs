# TableSeat

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for seats at the table that players occupy.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol TableSeat : Identifiable where Self.ID == TableSeatIdentifier
```

#### Overview

To represent seats in your game, follow these steps:

1. Create a structure that conforms to this protocol.
2. Set the [`State`](tableseat/state.md) type alias to [`TableSeatState`](tableseatstate.md).
3. Declare the `id` property as a [`TableSeatIdentifier`](tableseatidentifier.md) structure.
4. Declare the [`initialState`](tableseat/initialstate.md) property as a [`State`](tableseat/state.md) structure.
5. Implement an initializer that sets these properties.

```swift
struct Seat: TableSeat {
    typealias State = TableSeatState
    var id: TableSeatIdentifier
    var initialState: State

    init(index: Int = 0, position: TableVisualState.Point2D) {
        id = .seat(index)
        initialState = .init(pose: .init(position: position, rotation: .init()))
    }
}
```

Then add the seats to the [`TableSetup`](tablesetup.md) object using one of its add methods. For example, use the [`add(seat:)`](tablesetup/add(seat:)-a9qw.md) method to specify a position for the seat.

```swift
var setup = TableSetup(tabletop: table)
setup.add(seat: Seat(index: 0, position: .init(x: 0, z: -0.5)))
```

To render seats using RealityKit, conform to the [`EntityTableSeat`](entitytableseat.md) protocol instead.

## Topics

### Getting the seat data
- [var initialState: Self.State](tableseat/initialstate.md)
- [associatedtype State : SeatState](tableseat/state.md)

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
### Inherited By
- [EntityTableSeat](entitytableseat.md)

## See Also

- [struct TableState](tablestate.md)
  The state of the table that can be queried and modified.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tableseat)*