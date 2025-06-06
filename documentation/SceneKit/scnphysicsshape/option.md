# SCNPhysicsShape.Option

**Framework**: SceneKit  
**Kind**: struct

Keys for the options dictionary used when creating a physics shape.

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
struct Option
```

#### Discussion

When SceneKit creates a shape from a hierarchy of nodes containing multiple geometries, the [`keepAsCompound`](scnphysicsshape/option/keepascompound.md) option takes precedence over the [`type`](scnphysicsshape/option/type.md) option.

For example, if you have a node hierarchy containing several geometries, setting the the [`type`](scnphysicsshape/option/type.md) option to [`boundingBox`](scnphysicsshape/shapetype/boundingbox.md) and the [`keepAsCompound`](scnphysicsshape/option/keepascompound.md) option to [`true`](https://developer.apple.com/documentation/swift/true) creates a shape that is a combination of several boxes. This approach can provide better simulation performance than converting the entire node hierarchy to a single concave polyhedron shape.

## Topics

### Type Properties
- [static let collisionMargin: SCNPhysicsShape.Option](scnphysicsshape/option/collisionmargin.md)
- [static let keepAsCompound: SCNPhysicsShape.Option](scnphysicsshape/option/keepascompound.md)
  An option for selecting whether to create a group of independent shapes or combine them into a single shape.
- [static let scale: SCNPhysicsShape.Option](scnphysicsshape/option/scale.md)
  An option for selecting the scale factor of the shape relative to the local coordinate space of the node containing it.
- [static let type: SCNPhysicsShape.Option](scnphysicsshape/option/type.md)
  An option for selecting the level of detail at which to create shapes from geometry.
- [SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype.md)
  Values for the [`type`](scnphysicsshape/option/type.md) key specifying the level of detail that SceneKit uses when creating a physics shape based on a geometry.
### Initializers
- [init(rawValue: String)](scnphysicsshape/option/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option)*