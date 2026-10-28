# init(node:options:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a physics shape from a node or hierarchy of nodes.

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
convenience init(node: SCNNode, options: [SCNPhysicsShape.Option : Any]? = nil)
```

```objc
+ (instancetype) shapeWithNode:(SCNNode *) node options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A new physics shape object.

## Discussion

To use the newly created physics shape, create a physics body with the the [`init(type:shape:)`](../scnphysicsbody/init%28type,shape%29.md) method, or assign the shape to the [`physicsShape`](../scnphysicsbody/physicsshape.md) property of an existing body.

The node used to create the physics shape need not be the same as the node whose physics body you attach the shape to—or even be in the scene whose physics world you use the shape in. For example, you can create a physics body for a complex object by building a hierarchy of nodes containing simple geometries (using the [`SCNBox`](../scnbox.md) and [`SCNSphere`](../scnsphere.md) classes), and then creating a physics shape from those nodes. The resulting physics shape, a compound of bounding boxes or convex hulls, provides a rough approximation of the complex object without a high cost to simulation performance.

## Parameters

- `node`: A node object. The node must contain an [`SCNGeometry`](../scngeometry.md) object in its [`geometry`](../scnnode/geometry.md) property or have one or more child (or descendant) nodes that contain geometry.
- `options`: A dictionary of options affecting the level of detail of the physics shape, or `nil` to use default options. For applicable keys and their possible values, see `Shape Creation Options Keys`.

## See Also

### Creating Physics Shapes
- [convenience init(geometry: SCNGeometry, options: [SCNPhysicsShape.Option : Any]?)](./init%28geometry,options%29.md)
  Creates a physics shape based on a geometry object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/init(node:options:))*