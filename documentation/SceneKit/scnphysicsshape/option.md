# SCNPhysicsShape.Option

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Keys for the options dictionary used when creating a physics shape.

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
struct Option
```

```c
typedef NSString * SCNPhysicsShapeOption;
```

#### Discussion

When SceneKit creates a shape from a hierarchy of nodes containing multiple geometries, the [`keepAsCompound`](./option/keepascompound.md) option takes precedence over the [`type`](./option/type.md) option.

For example, if you have a node hierarchy containing several geometries, setting the the [`type`](./option/type.md) option to [`boundingBox`](./shapetype/boundingbox.md) and the [`keepAsCompound`](./option/keepascompound.md) option to [`true`](../../Swift/true.md) creates a shape that is a combination of several boxes. This approach can provide better simulation performance than converting the entire node hierarchy to a single concave polyhedron shape.

## Topics

### Type Properties
- [static let collisionMargin: SCNPhysicsShape.Option](./option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](./option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](./option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](./option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.
- [SCNPhysicsShape.ShapeType](./shapetype.md)
  Values for the [`type`](./option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.
### Initializers
- [init(rawValue: String)](./option/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option)*