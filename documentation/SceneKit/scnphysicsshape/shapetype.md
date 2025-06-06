# SCNPhysicsShape.ShapeType

**Framework**: SceneKit  
**Kind**: struct

Values for the [`type`](scnphysicsshape/option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct ShapeType
```

## Topics

### Type Properties
- [static let boundingBox: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.
### Initializers
- [init(rawValue: String)](scnphysicsshape/shapetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let collisionMargin: SCNPhysicsShape.Option](scnphysicsshape/option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](scnphysicsshape/option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](scnphysicsshape/option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](scnphysicsshape/option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype)*