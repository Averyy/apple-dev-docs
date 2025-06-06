# EntityTabletop

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for the table surface in your game when you render it using RealityKit.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EntityTabletop : Tabletop
```

#### Overview

To create a [`TableSetup`](tablesetup.md) object that configures your game table, pass an object that conforms to either the [`Tabletop`](tabletop.md) or `EntityTabletop` protocol to the `TableSetup` initializer. If you render your table surface using RealityKit, conform to the `EntityTabletop` protocol. Implement your `EntityTabletop` structure to set the protocol properties, such as the `shape`, `entity`, and `id` properties.

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

## Topics

### Creating a round or rectangular table
- [var shape: TabletopShape](entitytabletop/shape.md)
### Displaying the tabletop
- [var entity: Entity](entitytabletop/entity.md)
  The entity associated with the equipment.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
- [Tabletop](tabletop.md)

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/entitytabletop)*