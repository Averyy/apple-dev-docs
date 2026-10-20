# keepAsCompound

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option for selecting whether to create a group of independent shapes or combine them into a single shape.

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
static let keepAsCompound: SCNPhysicsShape.Option
```

```c
extern SCNPhysicsShapeOption const SCNPhysicsShapeKeepAsCompoundKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a Boolean value. The default value is [`true`](../../../Swift/true.md), specifying that SceneKit convert separate geometries into separate shapes and join the resulting shapes. If [`false`](../../../Swift/false.md), SceneKit creates a single shape approximating the combined form of the geometries.

## See Also

### Type Properties
- [static let collisionMargin: SCNPhysicsShape.Option](./collisionmargin.md)
- [static let scale: SCNPhysicsShape.Option](./scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](./type.md)
  An option for selecting the level of detail at which to create shapes from geometry.
- [SCNPhysicsShape.ShapeType](../shapetype.md)
  Values for the [`type`](./type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/keepascompound)*