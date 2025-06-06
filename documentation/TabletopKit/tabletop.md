# Tabletop

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for the table surface in your game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol Tabletop : Identifiable where Self.ID == EquipmentIdentifier
```

#### Overview

To create a [`TableSetup`](tablesetup.md) object that configures your game table, pass an object that conforms to either the `Tabletop` or `EntityTabletop`` protocol to the `TableSetup`initializer. Implement your`Tabletop`structure to set the protocol properties, such as the`shape`and`id` properties.

```swift
struct Table: Tabletop {
    var shape = .rectangular(width: 100, height: 60, thickness: 5, in: .centimeters)
    var id = .table
}
```

To create a round table, use one of the [`TabletopShape`](tabletopshape.md) round initializers.

To render the table surface using RealityKit, conform to the [`EntityTabletop`](entitytabletop.md) protocol instead.

## Topics

### Creating a round or rectangular table
- [var shape: TabletopShape](tabletop/shape.md)
### Displaying the equipment
- [func layoutChildren(for: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout](tabletop/layoutchildren(for:visualstate:).md)
  This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
### Inherited By
- [EntityTabletop](entitytabletop.md)

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletop)*