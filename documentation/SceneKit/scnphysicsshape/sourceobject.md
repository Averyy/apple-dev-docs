# sourceObject

**Framework**: SceneKit  
**Kind**: property

The object that was used to create the shape.

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
var sourceObject: Any { get }
```

#### Discussion

This property, along with the [`transforms`](scnphysicsshape/transforms.md) and [`options`](scnphysicsshape/options.md) properties, provides the information that was used to create the shape. You can use this information, for example, to draw editing or debugging UI in your scene.

- If the shape was created with the [`init(geometry:options:)`](scnphysicsshape/init(geometry:options:).md) method, the source object is an [`SCNGeometry`](scngeometry.md) object, and the [`options`](scnphysicsshape/options.md) property contains the options affecting the shape’s construction from that geometry.
- If the shape was created with the [`init(node:options:)`](scnphysicsshape/init(node:options:).md) method, the source object is an [`SCNNode`](scnnode.md) object, and the [`options`](scnphysicsshape/options.md) property contains the options affecting the shape’s construction from that node.
- If the shape was created with the [`init(shapes:transforms:)`](scnphysicsshape/init(shapes:transforms:).md) method, the source object is an array of [`SCNPhysicsShape`](scnphysicsshape.md) objects and the [`transforms`](scnphysicsshape/transforms.md) property describes how those shapes combine to form a compound shape.

## See Also

- [var options: [SCNPhysicsShape.Option : Any]?](scnphysicsshape/options.md)
  The options dictionary that was used to create the shape.
- [var transforms: [NSValue]?](scnphysicsshape/transforms.md)
  The array of transforms that was used to create a compound shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/sourceobject)*