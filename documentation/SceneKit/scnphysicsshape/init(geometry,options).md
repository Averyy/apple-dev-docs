# init(geometry:options:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a physics shape based on a geometry object.

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
convenience init(geometry: SCNGeometry, options: [SCNPhysicsShape.Option : Any]? = nil)
```

```objc
+ (instancetype) shapeWithGeometry:(SCNGeometry *) geometry options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A new physics shape object.

#### Discussion

If you create a physics shape using one of the basic geometry classes ([`SCNBox`](../scnbox.md), [`SCNSphere`](../scnsphere.md), [`SCNPyramid`](../scnpyramid.md), [`SCNCone`](../scncone.md), [`SCNCylinder`](../scncylinder.md), or [`SCNCapsule`](../scncapsule.md)), SceneKit uses an idealized form of that geometry for the physics shape instead of using the geometry’s vertex data to simulate collisions. For example, if you create a physics shape from an [`SCNSphere`](../scnsphere.md) object, SceneKit simulates collisions for any object that passes within the sphere’s radius.

Because the idealized forms of simple geometries are computationally much simpler than the vertex data needed for displaying them, using basic geometries for physics shapes (or compound shapes created from basic geometries with the [`init(shapes:transforms:)`](./init%28shapes,transforms%29.md) method) often provides the best balance between simulation accuracy and performance.

To use the newly created physics shape, create a physics body with the the [`init(type:shape:)`](../scnphysicsbody/init%28type,shape%29.md) method, or assign the shape to the [`physicsShape`](../scnphysicsbody/physicsshape.md) property of an existing body.

## Parameters

- `geometry`: A geometry object.
- `options`: A dictionary of options affecting the level of detail of the physics shape, or `nil` to use default options. For applicable keys and their possible values, see `Shape Creation Options Keys`.

## See Also

### Creating Physics Shapes
- [convenience init(node: SCNNode, options: [SCNPhysicsShape.Option : Any]?)](./init%28node,options%29.md)
  Creates a physics shape from a node or hierarchy of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/init(geometry:options:))*