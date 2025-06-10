# scale

**Framework**: SceneKit  
**Kind**: property

An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let scale: SCNPhysicsShape.Option
```

#### Discussion

The value for this key is an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object containing an [`SCNVector3`](scnvector3.md) structure, whose components describe the scale factor in each of the x-, y- and z-axis directions. The default value is the vector `{1.0, 1.0, 1.0}`, specifying no change of scale.

SceneKit’s physics simulation ignores the [`scale`](scnnode/scale.md) property of nodes containing physics bodies when simulating collisions. Instead, use this option to provide a scale factor when creating custom physics shapes. (If you create a physics body for a node without specifying a custom shape, SceneKit uses the node’s [`scale`](scnnode/scale.md) property to infer this scale factor at creation time.)

## See Also

- [static let collisionMargin: SCNPhysicsShape.Option](scnphysicsshape/option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](scnphysicsshape/option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let type: SCNPhysicsShape.Option](scnphysicsshape/option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.
- [SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype.md)
  Values for the [`type`](scnphysicsshape/option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/scale)*