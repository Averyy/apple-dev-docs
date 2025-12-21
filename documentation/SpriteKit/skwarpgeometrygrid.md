# SKWarpGeometryGrid

**Framework**: SpriteKit  
**Kind**: class

A definition for a grid-based deformation of nodes that conform to [`SKWarpable`](skwarpable.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SKWarpGeometryGrid
```

## Mentions

- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
- [Warping SpriteKit Content By Using an Effect Node](warping-spritekit-content-by-using-an-effect-node.md)

#### Overview

An `SKWarpGeometryGrid` exposes a 2D array of source positions, and set of destination positions with matching size, that allow you to define which sections of a node should be translated from the source positions to the destination positions. Conceptually, this forms two grids—a source grid and a destination grid—where the visual warping is accomplished by stretching or shrinking each section of the node as the source positions of the grid interpolate to their corresponding destination positions.

## Topics

### Creating a Warp Geometry Grid
- [convenience init(columns: Int, rows: Int)](skwarpgeometrygrid/init(columns:rows:).md)
  Creates a warp geometry grid of a specified size.
- [convenience init(columns: Int, rows: Int, sourcePositions: [SIMD2<Float>], destinationPositions: [SIMD2<Float>])](skwarpgeometrygrid/init(columns:rows:sourcepositions:destinationpositions:).md)
  Creates a warp geometry grid of a specific size and warp translation, in point arrays.
- [init?(coder: NSCoder)](skwarpgeometrygrid/init(coder:).md)
  Tells you when to intialize a grid that was loaded from an archive.
### Animating Warping
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
  Interpolate warping from source to destination warp geometry grids.
### Accessing or Setting Warp Geometry Grid Size
- [var numberOfColumns: Int](skwarpgeometrygrid/numberofcolumns.md)
  The object’s number of columns.
- [var numberOfRows: Int](skwarpgeometrygrid/numberofrows.md)
  The object’s number of rows.
- [var vertexCount: Int](skwarpgeometrygrid/vertexcount.md)
  The object’s total number of vertices.
### Accessing or Setting Grid Vertices
- [func destPosition(at: Int) -> vector_float2](skwarpgeometrygrid/destposition(at:).md)
  Returns the destination position of a vertex.
- [func replacingByDestinationPositions(positions: [SIMD2<Float>]) -> SKWarpGeometryGrid](skwarpgeometrygrid/replacingbydestinationpositions(positions:).md)
  Returns a copy of this grid, updated with the argument destination positions.
- [func replacingBySourcePositions(positions: [SIMD2<Float>]) -> SKWarpGeometryGrid](skwarpgeometrygrid/replacingbysourcepositions(positions:).md)
  Returns a copy of this grid, updated with the argument source positions.
- [func sourcePosition(at: Int) -> vector_float2](skwarpgeometrygrid/sourceposition(at:).md)
  Returns the source position of a vertex.

## Relationships

### Inherits From
- [SKWarpGeometry](skwarpgeometry.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKWarpGeometry](skwarpgeometry.md)
  A definition for a deformation of nodes that conform to [`SKWarpable`](skwarpable.md).
- [protocol SKWarpable](skwarpable.md)
  A protocol for objects that can be warped and animated by an [`SKWarpGeometry`](skwarpgeometry.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid)*