# SCNPhysicsShape.ShapeType

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Values for the [`type`](./option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
struct ShapeType
```

```c
typedef NSString * SCNPhysicsShapeType;
```

## Topics

### Type Properties
- [static let boundingBox: SCNPhysicsShape.ShapeType](./shapetype/boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](./shapetype/concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](./shapetype/convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.
### Initializers
- [init(rawValue: String)](./shapetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Type Properties
- [static let collisionMargin: SCNPhysicsShape.Option](./option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](./option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](./option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](./option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype)*