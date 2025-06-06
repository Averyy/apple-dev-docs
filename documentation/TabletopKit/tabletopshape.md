# TabletopShape

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the physical properties of the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TabletopShape
```

#### Overview

To create a round table, use the [`round(center:radius:thickness:in:)`](tabletopshape/round(center:radius:thickness:in:).md) initializer, or if you render the table using RealityKit, the [`round(entity:)`](tabletopshape/round(entity:).md) initializer. For a rectangular table, use the equivalent [`rectangular(center:width:height:thickness:in:)`](tabletopshape/rectangular(center:width:height:thickness:in:).md) or [`rectangular(entity:)`](tabletopshape/rectangular(entity:).md) initializer.

## Topics

### Creating a round or rectangular table
- [static func rectangular(center: Point3D, width: Float, height: Float, thickness: Float, in: UnitLength) -> TabletopShape](tabletopshape/rectangular(center:width:height:thickness:in:).md)
  Creates a rectangular tabletop shape with the specified center and dimensions.
- [static func round(center: Point3D, radius: Float, thickness: Float, in: UnitLength) -> TabletopShape](tabletopshape/round(center:radius:thickness:in:).md)
  Creates a round tabletop shape with the specified center, radius, and thickness.
### Creating a table that you render using an entity
- [static func rectangular(entity: Entity) -> TabletopShape](tabletopshape/rectangular(entity:).md)
- [static func round(entity: Entity) -> TabletopShape](tabletopshape/round(entity:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopshape)*