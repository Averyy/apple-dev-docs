# TabletopShape

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the physical properties of the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TabletopShape
```

#### Overview

To create a round table, use the [`round(center:radius:thickness:in:)`](./tabletopshape/round%28center,radius,thickness,in%29.md) initializer, or if you render the table using RealityKit, the [`round(entity:)`](./tabletopshape/round%28entity%29.md) initializer. For a rectangular table, use the equivalent [`rectangular(center:width:height:thickness:in:)`](./tabletopshape/rectangular%28center,width,height,thickness,in%29.md) or [`rectangular(entity:)`](./tabletopshape/rectangular%28entity%29.md) initializer.

## Topics

### Creating a round or rectangular table
- [static func rectangular(center: Point3D, width: Float, height: Float, thickness: Float, in: UnitLength) -> TabletopShape](./tabletopshape/rectangular%28center,width,height,thickness,in%29.md)
  Creates a rectangular tabletop shape with the specified center and dimensions.
- [static func round(center: Point3D, radius: Float, thickness: Float, in: UnitLength) -> TabletopShape](./tabletopshape/round%28center,radius,thickness,in%29.md)
  Creates a round tabletop shape with the specified center, radius, and thickness.
### Creating a table that you render using an entity
- [static func rectangular(entity: Entity) -> TabletopShape](./tabletopshape/rectangular%28entity%29.md)
- [static func round(entity: Entity) -> TabletopShape](./tabletopshape/round%28entity%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Creating tabletop games](./creating-tabletop-games.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [Synchronizing group gameplay with TabletopKit](./synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.
- [class TabletopGame](./tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](./tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](./tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](./entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopshape)*