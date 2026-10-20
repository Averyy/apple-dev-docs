# type

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option for selecting the level of detail at which to create shapes from geometry.

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
static let type: SCNPhysicsShape.Option
```

```c
extern SCNPhysicsShapeOption const SCNPhysicsShapeTypeKey;
```

#### Discussion

The value for this key is one of the constants listed in `Shape Types`. The default type is [`convexHull`](../shapetype/convexhull.md).

## See Also

### Type Properties
- [static let collisionMargin: SCNPhysicsShape.Option](./collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](./keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](./scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [SCNPhysicsShape.ShapeType](../shapetype.md)
  Values for the [`type`](./type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/type)*