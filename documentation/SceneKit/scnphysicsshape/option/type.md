# type

**Framework**: SceneKit  
**Kind**: property

An option for selecting the level of detail at which to create shapes from geometry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let type: SCNPhysicsShape.Option
```

#### Discussion

The value for this key is one of the constants listed in `Shape Types`. The default type is [`convexHull`](scnphysicsshape/shapetype/convexhull.md).

## See Also

- [static let collisionMargin: SCNPhysicsShape.Option](scnphysicsshape/option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](scnphysicsshape/option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](scnphysicsshape/option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype.md)
  Values for the [`type`](scnphysicsshape/option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/type)*