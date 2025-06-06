# TableSetup

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the arrangement of seats, equipment, and counters around the game table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableSetup
```

#### Overview

To create a `TableSetup` object, pass an object that conforms to the [`Tabletop`](tabletop.md) or [`EntityTabletop`](entitytabletop.md) protocol to the [`init(tabletop:)`](tablesetup/init(tabletop:)-4cfut.md) initializer. For example, implement a `Table` structure that conforms to the `EntityTabletop` protocol and pass an instance of it to the initializer.

```swift
let table = Table()
root = createRootEntity(table: table.entity)
var setup = TableSetup(tabletop: table)
```

Set the protocol properties, such as `shape`, `entity`, and `id` properties for the `EntityTabletop` protocol, in the initializer.

```swift
struct Table: EntityTabletop {
    var shape: TabletopShape
    var entity: Entity
    var id: EquipmentIdentifier
    
    init() {
        self.entity = try! Entity.load(named: "table/table", in: contentBundle)
        self.shape = .round(entity: entity)
        self.id = .table
    }
}
```

Then add seats, equipment, and counters to the `TableSetup` object.

To represent seats, create structures that conform to a seat protocol. To render seats using RealityKit, conform to the [`EntityTableSeat`](entitytableseat.md) protocol and use the [`add(seat:)`](tablesetup/add(seat:)-4alrc.md) or a similar method to add seats. Otherwise, conform to the [`TableSeat`](tableseat.md) protocol and use the [`add(seat:)`](tablesetup/add(seat:)-a9qw.md) or a similar method to add seats.

```swift
setup.add(seat: Seat(index: 0, position: .init(x: 0, z: -0.5)))
setup.add(seat: Seat(index: 1, position: .init(x: 0, z: +0.5)))
```

To represent equipment, create structures that conform to an equipment protocol. To render equipment using RealityKit, conform to the [`EntityEquipment`](entityequipment.md) protocol and use the [`add(equipment:)`](tablesetup/add(equipment:)-24tv6.md) or a similar method to add equipment. Otherwise, conform to the [`Equipment`](equipment.md) protocol and use the [`add(equipment:)`](tablesetup/add(equipment:)-29pef.md) or a similar method to add equipment.

```swift
setup.add(equipment: Piece(position: .init(x: 0, z: 0.1)))
setup.add(equipment: Card(index: 0, faceUp: true, position: .init(x: -0.1, z: 0)))
setup.add(equipment: Card(index: 1, faceUp: true, position: .init(x: +0.1, z: 0)))
setup.add(equipment: Die(index: 0, position: .init(x: 0, z: 0.2)))
```

Some equipment can represent a group, such as a player’s hand in a card game. To organize equipment hierarchically, set the [`parentID`](equipmentstate/parentid.md) property of the [`State`](equipment/state.md) property during gameplay. In your equipment structure implementation, you can override the [`layoutChildren(for:visualState:)`](equipment/layoutchildren(for:visualstate:).md) method to lay out the containing equipment.

Optionally, add one or more [`ScoreCounter`](scorecounter.md) objects to the `TableSetup` object to keep score of the game. Use either the [`add(counter:)`](tablesetup/add(counter:).md) or [`add(counters:)`](tablesetup/add(counters:).md) method to add score counters.

Finally, create the [`TabletopGame`](tabletopgame.md) instance from the `TableSetup` object by passing it to the [`init(tableSetup:version:)`](tabletopgame/init(tablesetup:version:).md) initializer.

```swift
game = TabletopGame(tableSetup: setup)
```

## Topics

### Creating a setup object from a table
- [init(tabletop: some Tabletop)](tablesetup/init(tabletop:)-4cfut.md)
- [init(tabletop: some EntityTabletop)](tablesetup/init(tabletop:)-7ima6.md)
### Adding seats to place players
- [func add(seat: some TableSeat)](tablesetup/add(seat:)-a9qw.md)
- [func add(seat: some EntityTableSeat)](tablesetup/add(seat:)-4alrc.md)
- [func add(seats: some Sequence)](tablesetup/add(seats:)-4068d.md)
- [func add(seats: some Sequence)](tablesetup/add(seats:)-4asnu.md)
### Adding equipment for gameplay
- [func add(equipment: some Equipment)](tablesetup/add(equipment:)-29pef.md)
- [func add(equipment: some EntityEquipment)](tablesetup/add(equipment:)-24tv6.md)
- [func add(equipment: some Sequence)](tablesetup/add(equipment:)-4k6m6.md)
- [func add(equipment: some Sequence)](tablesetup/add(equipment:)-9syh2.md)
### Adding counters to keep score
- [func add(counter: ScoreCounter)](tablesetup/add(counter:).md)
- [func add(counters: some Sequence<ScoreCounter>)](tablesetup/add(counters:).md)

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup)*