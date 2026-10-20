# sphere(radius:in:restitution:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

Creates a sphere with the specified radius that the player tosses during gameplay.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func sphere(radius: Float, in unit: UnitLength = .meters, restitution: Float? = nil) -> TossableRepresentation
```

#### Discussion

Higher restitution values indicate materials that conserve kinetic energy during collisions, causing objects to bounce off each other elastically. Lower values suggest materials that absorb kinetic energy, resulting in less bounce and more energy loss upon impact.

## Parameters

- `radius`: The radius of the sphere.
- `unit`: The unit of measurement for the radius.
- `restitution`: The coefficient of restitution, in the range [0, 1].

## See Also

### Creating geometric shapes
- [static func cube(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./cube%28height,in,restitution%29.md)
  Creates a cube that the player tosses during gameplay.
- [static func decahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./decahedron%28height,in,restitution%29.md)
  Creates a decahedron, a symmetrical, ten-faced polyhedron with kite-shaped faces, that the player tosses during gameplay.
- [static func dodecahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./dodecahedron%28height,in,restitution%29.md)
  Creates a regular dodecahedron, a shape with 12 pentagonal faces, that the player tosses during gameplay.
- [static func icosahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./icosahedron%28height,in,restitution%29.md)
  Creates a regular icosahedron, a shape with 20 triangular faces, that the player tosses during gameplay.
- [static func octahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./octahedron%28height,in,restitution%29.md)
  Creates a regular octahedron, a shape with 8 triangular faces, that the player tosses during gameplay.
- [static func tetrahedron(height: Float, in: UnitLength, restitution: Float?) -> TossableRepresentation](./tetrahedron%28height,in,restitution%29.md)
  Creates a regular tetrahedron, a pyramid with four triangular faces, that the player tosses during gameplay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/sphere(radius:in:restitution:))*