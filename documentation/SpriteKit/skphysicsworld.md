# SKPhysicsWorld

**Framework**: SpriteKit  
**Kind**: class

The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.

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
class SKPhysicsWorld
```

## Mentions

- [Disconnecting Bodies from Joints](disconnecting-bodies-from-joints.md)
- [Connecting Bodies with Joints](connecting-bodies-with-joints.md)
- [Getting Started with Physics](getting-started-with-physics.md)

#### Overview

`SKPhysicsWorld` runs the physics engine of a scene and is the place that contact detection occurs. Do not create a `SKPhysicsWorld` directly; the system creates a physics world and adds it to the scene’s [`physicsWorld`](skscene/physicsworld.md) property.

The physics world allows you to:

- Set important properties like [`gravity`](skphysicsworld/gravity.md)
- Join two physics bodies using an [`SKPhysicsJoint`](skphysicsjoint.md)
- Respond to collision between two physics bodies using [`contactDelegate`](skphysicsworld/contactdelegate.md)
- Do custom collisions detection or hit testing

## Topics

### Configuring the Physics World
- [var gravity: CGVector](skphysicsworld/gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](skphysicsworld/speed.md)
  The rate at which the simulation executes.
### Joining Physics Bodies with Joints
- [func add(SKPhysicsJoint)](skphysicsworld/add(_:).md)
  Adds a joint to the physics world.
- [func removeAllJoints()](skphysicsworld/removealljoints.md)
  Removes all joints from the physics world.
- [func remove(SKPhysicsJoint)](skphysicsworld/remove(_:).md)
  Removes a specific joint from the physics world.
### Detecting Collisions
- [var contactDelegate: (any SKPhysicsContactDelegate)?](skphysicsworld/contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
### Searching the Scene for Physics Bodies
- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(alongraystart:end:).md)
  Searches for the first physics body that intersects a ray.
- [func body(at: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(at:).md)
  Searches for the first physics body that contains a point.
- [func body(in: CGRect) -> SKPhysicsBody?](skphysicsworld/body(in:).md)
  Searches for the first physics body that intersects the specified rectangle.
- [func enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(alongraystart:end:using:).md)
  Enumerates all the physics bodies in the scene that intersect a ray.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(at:using:).md)
  Enumerates all the physics bodies in the scene that contain a point.
- [func enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(in:using:).md)
  Enumerates all the physics bodies in the scene that intersect the specified rectangle.
### Sampling Physics Fields
- [func sampleFields(at: vector_float3) -> vector_float3](skphysicsworld/samplefields(at:).md)
  Samples all of the field nodes in the scene and returns the summation of their forces at that point.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsBody](skphysicsbody.md)
  An object that adds physics simulation to a node.
- [class SKPhysicsContact](skphysicscontact.md)
  A description of the contact between two physics bodies.
- [protocol SKPhysicsContactDelegate](skphysicscontactdelegate.md)
  Methods your app can implement to respond when physics bodies come into contact.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld)*