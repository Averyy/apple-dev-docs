# SCNPhysicsShape

**Framework**: SceneKit  
**Kind**: class

An abstraction of a physics body’s solid volume for tuning collision detection.

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
class SCNPhysicsShape
```

#### Overview

When SceneKit performs contact detection and other simulations for the [`SCNPhysicsBody`](scnphysicsbody.md) objects in your scene, it uses physics shapes instead of the rendered geometry of visible objects. This approach both improves simulation performance and allows you to more easily design your gameplay around scene elements the player can interact with.

##### Simple Versus Complex Shapes

When you allow SceneKit to automatically create a physics shape, it uses the simplest possible shape roughly matching the geometry of the node the physics body is attached to. This approach maximizes simulation performance but can lead to unrealistic physics behavior for some objects.

You can make the simulation behave more realistically by defining physics shapes that more closely follow the visible geometry in your scene. This approach comes at a cost to performance, so you want to limit the amount of detail in your physics shapes. Use the highest levels of detail only on bodies for which precise collision detection is important for your app.

If you create a physics shape using one of the basic geometry classes ([`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), or [`SCNCapsule`](scncapsule.md)), SceneKit uses an idealized form of that geometry for the physics shape instead of using the geometry’s vertex data to simulate collisions. For example, if you create a physics shape from an [`SCNSphere`](scnsphere.md) object, SceneKit simulates collisions for any object that passes within the sphere’s radius.

Because the idealized forms of simple geometries are computationally much simpler than the vertex data needed for displaying them, using basic geometries for physics shapes (or compound shapes created from basic geometries with the [`init(shapes:transforms:)`](scnphysicsshape/init(shapes:transforms:).md) method) often provides the best balance between simulation accuracy and performance.

##### Changing a Physics Bodys Shape

Physics shapes are immutable, but you can change the shape associated with a physics body by creating a new [`SCNPhysicsShape`](scnphysicsshape.md) instance and assigning it to the body’s [`physicsShape`](scnphysicsbody/physicsshape.md) property.

## Topics

### Creating Physics Shapes
- [convenience init(geometry: SCNGeometry, options: [SCNPhysicsShape.Option : Any]?)](scnphysicsshape/init(geometry:options:).md)
  Creates a physics shape based on a geometry object.
- [convenience init(node: SCNNode, options: [SCNPhysicsShape.Option : Any]?)](scnphysicsshape/init(node:options:).md)
  Creates a physics shape from a node or hierarchy of nodes.
### Combining Physics Shapes
- [convenience init(shapes: [SCNPhysicsShape], transforms: [NSValue]?)](scnphysicsshape/init(shapes:transforms:).md)
  Creates a new physics shape by combining others.
### Getting Information About a Shape
- [var sourceObject: Any](scnphysicsshape/sourceobject.md)
  The object that was used to create the shape.
- [var options: [SCNPhysicsShape.Option : Any]?](scnphysicsshape/options.md)
  The options dictionary that was used to create the shape.
- [var transforms: [NSValue]?](scnphysicsshape/transforms.md)
  The array of transforms that was used to create a compound shape.
### Shape Options
- [SCNPhysicsShape.Option](scnphysicsshape/option.md)
  Keys for the options dictionary used when creating a physics shape.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsBody](scnphysicsbody.md)
  The physics simulation attributes attached to a scene graph node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape)*