# kinematic()

**Framework**: SceneKit  
**Kind**: method

Creates a physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.

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
class func kinematic() -> Self
```

#### Return Value

A new physics body object.

#### Discussion

Use kinematic bodies for scene elements that you want to control directly but whose movement manipulates other elements. For example, to allow the user to push objects around with a finger, you might create a kinematic body and attach it to an invisible node that you move follow touch events. (In macOS, use the same technique to allow the user to move objects with the mouse pointer.)

For the body to participate in collision detection or respond to forces, you must attach it to the [`physicsBody`](scnnode/physicsbody.md) property of an [`SCNNode`](scnnode.md) object in a scene.

SceneKit automatically creates a physics shape for the body when you attach it to a node, based on that node’s [`geometry`](scnnode/geometry.md) property. To create a physics shape that’s based on the geometries of a node and its hierarchy of children, or to control the level of detail in a physics shape, create the physics shape manually using an [`SCNPhysicsShape`](scnphysicsshape.md) class method.

> **Note**:  For nodes containing custom geometry, the physics shape SceneKit automatically creates is a rough approximation of the geometry. This approximation, or , provides a compromise between accuracy and performance in collision detection. For the best collision detection performance, create an [`SCNPhysicsShape`](scnphysicsshape.md) instance based on a basic geometry class ([`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), or [`SCNCapsule`](scncapsule.md)).

 For nodes containing custom geometry, the physics shape SceneKit automatically creates is a rough approximation of the geometry. This approximation, or , provides a compromise between accuracy and performance in collision detection. For the best collision detection performance, create an [`SCNPhysicsShape`](scnphysicsshape.md) instance based on a basic geometry class ([`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), or [`SCNCapsule`](scncapsule.md)).

## See Also

- [var type: SCNPhysicsBodyType](scnphysicsbody/type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [var physicsShape: SCNPhysicsShape?](scnphysicsbody/physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [convenience init(type: SCNPhysicsBodyType, shape: SCNPhysicsShape?)](scnphysicsbody/init(type:shape:).md)
  Creates a physics body with the specified type and shape.
- [class func `static`() -> Self](scnphysicsbody/static.md)
  Creates a physics body that is unaffected by forces or collisions and that cannot move.
- [class func dynamic() -> Self](scnphysicsbody/dynamic.md)
  Creates a physics body that can be affected by forces and collisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/kinematic())*