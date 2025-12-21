# keepAsCompound

**Framework**: SceneKit  
**Kind**: property

An option for selecting whether to create a group of independent shapes or combine them into a single shape.

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
static let keepAsCompound: SCNPhysicsShape.Option
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`true`](https://developer.apple.com/documentation/Swift/true), specifying that SceneKit convert separate geometries into separate shapes and join the resulting shapes. If [`false`](https://developer.apple.com/documentation/Swift/false), SceneKit creates a single shape approximating the combined form of the geometries.

## See Also

- [static let collisionMargin: SCNPhysicsShape.Option](scnphysicsshape/option/collisionmargin.md)
- [static let scale: SCNPhysicsShape.Option](scnphysicsshape/option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](scnphysicsshape/option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.
- [SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype.md)
  Values for the [`type`](scnphysicsshape/option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/keepascompound)*