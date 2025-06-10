# TossableRepresentation

**Framework**: TabletopKit  
**Kind**: struct

An object that represents geometric shapes that the player can throw during gameplay, such as dice.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TossableRepresentation
```

## Topics

### Creating geometric shapes
- [static func cube(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/cube(height:in:restitution:).md)
  Creates a cube that the player tosses during gameplay.
- [static func decahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/decahedron(height:in:restitution:).md)
  Creates a decahedron, a symmetrical, ten-faced polyhedron with kite-shaped faces, that the player tosses during gameplay.
- [static func dodecahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/dodecahedron(height:in:restitution:).md)
  Creates a regular dodecahedron, a shape with 12 pentagonal faces, that the player tosses during gameplay.
- [static func icosahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/icosahedron(height:in:restitution:).md)
  Creates a regular icosahedron, a shape with 20 triangular faces, that the player tosses during gameplay.
- [static func octahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/octahedron(height:in:restitution:).md)
  Creates a regular octahedron, a shape with 8 triangular faces, that the player tosses during gameplay.
- [static func sphere(radius: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/sphere(radius:in:restitution:).md)
  Creates a sphere with the specified radius that the player tosses during gameplay.
- [static func tetrahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](tossablerepresentation/tetrahedron(height:in:restitution:).md)
  Creates a regular tetrahedron, a pyramid with four triangular faces, that the player tosses during gameplay.
### Protocols
- [TossableRepresentation.TossableFace](tossablerepresentation/tossableface.md)
  A protocol that represents a face of a tossable shape.
### Structures
- [TossableRepresentation.SphereFace](tossablerepresentation/sphereface.md)
  An object that represents an infinitely small area on the surface of a sphere (effectively a point).
### Instance Methods
- [func face(for: Rotation3D) -> any TossableRepresentation.TossableFace](tossablerepresentation/face(for:).md)
  For the shape corresponding to this tossable representation, constructs the face in contact with the table when the equipment has the given resting orientation.
### Enumerations
- [TossableRepresentation.CubeFace](tossablerepresentation/cubeface.md)
  One of the faces of a cube
- [TossableRepresentation.DecahedronFace](tossablerepresentation/decahedronface.md)
  One of the faces of an decahedron
- [TossableRepresentation.DodecahedronFace](tossablerepresentation/dodecahedronface.md)
  One of the faces of an dodecahedron
- [TossableRepresentation.IcosahedronFace](tossablerepresentation/icosahedronface.md)
  One of the faces of an icosahedron
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation)*