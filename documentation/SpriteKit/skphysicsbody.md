# SKPhysicsBody

**Framework**: SpriteKit  
**Kind**: class

An object that adds physics simulation to a node.

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
class SKPhysicsBody
```

## Mentions

- [Getting Started with Physics](getting-started-with-physics.md)
- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)
- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)

#### Overview

Assign a [`SKPhysicsBody`](skphysicsbody.md) object to the [`physicsBody`](sknode/physicsbody.md) property of the [`SKNode`](sknode.md) object to add physics simulation to the node. When a scene processes a new frame, it performs physics calculations on physics bodies attached to nodes in the scene. These calculations include gravity, friction, and collisions with other bodies. You can also apply your own forces and impulses to a body. After the scene completes these calculations, it updates the positions and orientations of the node objects.

> ❗ **Important**:  A physics body must be associated with a node before you apply forces or impulses to it.

SpriteKit supports two kinds of physics bodies,  and . When you create a physics body, its kind, size, and shape are determined by the constructor method you call. An edge-based body does not have mass or volume and is unaffected by forces or impulses in the system. Edge-based bodies are used to represent volumeless boundaries or hollow spaces in your physics simulation. In contrast, volume-based bodies are used to represent objects with mass and volume. The [`isDynamic`](skphysicsbody/isdynamic.md) property controls whether a volume-based body is affected by gravity, friction, collisions with other objects, and forces or impulses you directly apply to it.

The [`SKPhysicsBody`](skphysicsbody.md) class defines the physical characteristics for the body when it is simulated by the scene. For volume-based bodies, the most important property is the [`mass`](skphysicsbody/mass.md) property. A volume-based body is assumed to have a uniform density. You can either set the [`mass`](skphysicsbody/mass.md) property directly, or you can set the body’s [`density`](skphysicsbody/density.md) property and let the physics body calculate its own mass. All values in Sprite Kit are specified using the International System of Units (SI units). The actual forces and mass values are not important so long as your game uses consistent values.

When you design a game that uses physics, you define the different categories of physics objects that appear in the scene. You define up to 32 different categories of physics bodies, and a body can be assigned to as many of these categories as you want. In addition to declaring its own categories, a physics body also declares which categories of bodies it interacts with. See [`SKPhysicsBody`](skphysicsbody.md). You use a similar mechanism to declare which physics field nodes ([`SKFieldNode`](skfieldnode.md)) can affect the physics body.

For a volume-based body, you can dynamically control how the body is affected by forces or collisions. See [`SKPhysicsBody`](skphysicsbody.md).

## Topics

### First Steps
- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)
  Create and assign a physics body to enable physics.
### Creating a Body from a Shape
- [init(circleOfRadius: CGFloat)](skphysicsbody/init(circleofradius:).md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(circleOfRadius: CGFloat, center: CGPoint)](skphysicsbody/init(circleofradius:center:).md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](skphysicsbody/init(rectangleof:).md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](skphysicsbody/init(rectangleof:center:).md)
  Creates a rectangular physics body centered on an arbitrary point.
- [init(polygonFrom: CGPath)](skphysicsbody/init(polygonfrom:).md)
  Creates a polygonal physics body.
### Creating a Body from a Texture
- [Shaping a Physics Body to Match a Node’s Graphics](shaping-a-physics-body-to-match-a-node-s-graphics.md)
  Shape a physics body to your graphics for the right blend of collision accuracy and performance.
- [init(texture: SKTexture, size: CGSize)](skphysicsbody/init(texture:size:).md)
  Creates a physics body from the contents of a texture.
- [init(texture: SKTexture, alphaThreshold: Float, size: CGSize)](skphysicsbody/init(texture:alphathreshold:size:).md)
  Creates a physics body from the contents of a texture, capturing only the texels that exceed a specified transparency value.
### Creating a Body from a Collection of Bodies
- [init(bodies: [SKPhysicsBody])](skphysicsbody/init(bodies:).md)
  Creates a physics body that’s shaped like a union of the argument physics bodies.
### Creating an Edge-Based Physics Body
- [Creating an Edge Loop Around a Scene](creating-an-edge-loop-around-a-scene.md)
  Border your scene with an obstacle that physics bodies cannot penetrate.
- [init(edgeLoopFrom: CGRect)](skphysicsbody/init(edgeloopfrom:)-8sqfy.md)
  Creates an edge loop from a rectangle.
- [init(edgeFrom: CGPoint, to: CGPoint)](skphysicsbody/init(edgefrom:to:).md)
  Creates an edge between two points.
- [init(edgeLoopFrom: CGPath)](skphysicsbody/init(edgeloopfrom:)-5grxu.md)
  Creates an edge loop from a path.
- [init(edgeChainFrom: CGPath)](skphysicsbody/init(edgechainfrom:).md)
  Creates an edge chain from a path.
### Defining How Forces Affect a Physics Body
- [var affectedByGravity: Bool](skphysicsbody/affectedbygravity.md)
  A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.
- [var allowsRotation: Bool](skphysicsbody/allowsrotation.md)
  A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.
- [var isDynamic: Bool](skphysicsbody/isdynamic.md)
  A Boolean value that indicates whether the physics body is moved by the physics simulation.
### Defining a Physics Body’s Physical Properties
- [Configuring a Physics Body](configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](skphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var density: CGFloat](skphysicsbody/density.md)
  The density of the object, in kilograms per square meter.
- [var area: CGFloat](skphysicsbody/area.md)
  The area covered by the body.
- [var friction: CGFloat](skphysicsbody/friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](skphysicsbody/restitution.md)
  The bounciness of the physics body.
- [var linearDamping: CGFloat](skphysicsbody/lineardamping.md)
  A property that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](skphysicsbody/angulardamping.md)
  A property that reduces the body’s rotational velocity.
### Working with Collisions and Contacts
- [About Collisions and Contacts](about-collisions-and-contacts.md)
  Learn how to set up nodes for collision detection.
- [var categoryBitMask: UInt32](skphysicsbody/categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var collisionBitMask: UInt32](skphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var usesPreciseCollisionDetection: Bool](skphysicsbody/usesprecisecollisiondetection.md)
  A Boolean value that determines whether the physics world uses an iterative collision detection algorithm.
- [var contactTestBitMask: UInt32](skphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of physics bodies cause intersection notifications with this physics body.
- [func allContactedBodies() -> [SKPhysicsBody]](skphysicsbody/allcontactedbodies.md)
  The physics bodies that this physics body is in contact with.
### Applying Forces and Impulses to a Physics Body
- [Making Physics Bodies Move](making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](skphysicsbody/applyforce(_:).md)
  Applies a force to the center of gravity of a physics body.
- [func applyTorque(CGFloat)](skphysicsbody/applytorque(_:).md)
  Applies torque to an object.
- [func applyForce(CGVector, at: CGPoint)](skphysicsbody/applyforce(_:at:).md)
  Applies a force to a specific point of a physics body.
- [func applyImpulse(CGVector)](skphysicsbody/applyimpulse(_:).md)
  Applies an impulse to the center of gravity of a physics body.
- [func applyAngularImpulse(CGFloat)](skphysicsbody/applyangularimpulse(_:).md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](skphysicsbody/applyimpulse(_:at:).md)
  Applies an impulse to a specific point of a physics body.
### Inspecting a Physics Body’s Position and Velocity
- [var velocity: CGVector](skphysicsbody/velocity.md)
  The physics body’s velocity vector, measured in meters per second.
- [var angularVelocity: CGFloat](skphysicsbody/angularvelocity.md)
  The physics body’s angular speed.
- [var isResting: Bool](skphysicsbody/isresting.md)
  A Boolean property that indicates whether the object is at rest within the physics simulation.
### Reading a Physics Body’s Node
- [var node: SKNode?](skphysicsbody/node.md)
  The node that this body is connected to.
### Determining Which Joints Are Connected to a Physics Body
- [var joints: [SKPhysicsJoint]](skphysicsbody/joints.md)
  The joints connected to this physics body.
### Interacting with Physics Fields
- [var fieldBitMask: UInt32](skphysicsbody/fieldbitmask.md)
  A mask that defines which categories of physics fields can exert forces on this physics body.
- [var charge: CGFloat](skphysicsbody/charge.md)
  The electrical charge of the physics body.
### Pinning a Physics Body to a Node’s Parent
- [Pinning and Rotating Physics Bodies](pinning-and-rotating-physics-bodies.md)
  Pin a node so it’s free to rotate about a certain point on its parent node.
- [var pinned: Bool](skphysicsbody/pinned.md)
  A Boolean value that indicates whether the physics body’s node is pinned to its parent node.

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

- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsWorld](skphysicsworld.md)
  The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- [class SKPhysicsContact](skphysicscontact.md)
  A description of the contact between two physics bodies.
- [protocol SKPhysicsContactDelegate](skphysicscontactdelegate.md)
  Methods your app can implement to respond when physics bodies come into contact.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody)*