# sourceObject

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The object that was used to create the shape.

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
var sourceObject: Any { get }
```

```objc
@property (nonatomic, readonly) id sourceObject;
```

## Discussion

This property, along with the [`transforms`](./transforms.md) and [`options`](./options.md) properties, provides the information that was used to create the shape. You can use this information, for example, to draw editing or debugging UI in your scene.

- If the shape was created with the [`init(geometry:options:)`](./init%28geometry,options%29.md) method, the source object is an [`SCNGeometry`](../scngeometry.md) object, and the [`options`](./options.md) property contains the options affecting the shape’s construction from that geometry.
- If the shape was created with the [`init(node:options:)`](./init%28node,options%29.md) method, the source object is an [`SCNNode`](../scnnode.md) object, and the [`options`](./options.md) property contains the options affecting the shape’s construction from that node.
- If the shape was created with the [`init(shapes:transforms:)`](./init%28shapes,transforms%29.md) method, the source object is an array of [`SCNPhysicsShape`](../scnphysicsshape.md) objects and the [`transforms`](./transforms.md) property describes how those shapes combine to form a compound shape.

## See Also

### Getting Information About a Shape
- [var options: [SCNPhysicsShape.Option : Any]?](./options.md)
  The options dictionary that was used to create the shape.
- [var transforms: [NSValue]?](./transforms.md)
  The array of transforms that was used to create a compound shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/sourceobject)*