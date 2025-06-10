# SCNPhysicsBody

**Framework**: SceneKit  
**Kind**: class

The physics simulation attributes attached to a scene graph node.

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
class SCNPhysicsBody
```

#### Overview

When SceneKit prepares to render a new frame, it performs physics calculations on physics bodies attached to nodes in the scene. These calculations include gravity, friction, and collisions with other bodies. You can also apply your own forces and impulses to a body. After SceneKit completes these calculations, it updates the positions and orientations of the node objects before rendering the frame.

To add physics to a node, create and configure an [`SCNPhysicsBody`](scnphysicsbody.md) object and then assign it to the [`physicsBody`](scnnode/physicsbody.md) property of the [`SCNNode`](scnnode.md) object. A physics body must be associated with a node object before you apply forces or impulses to it.

##### A Bodys Physical Characteristics

The [`SCNPhysicsBody`](scnphysicsbody.md) class defines the physical characteristics for the body when it is simulated by the scene. Three properties are most important for physics simulation:

- The [`type`](scnphysicsbody/type.md) property, which determines how the body interacts with forces and other bodies in the simulation.  bodies are unaffected by forces and collisions and cannot move.  bodies are affected by forces and collisions with other body types.  bodies are not affected by forces or collisions, but by moving them directly you can cause collisions that affect dynamic bodies.
- The [`physicsShape`](scnphysicsbody/physicsshape.md) property, which defines the three-dimensional form of the body for collision detection purposes. Physics simulations run faster when using simple shapes instead of the fine detail of a node’s visible geometry. Typically, you set a body’s physics shape to a bounding box, sphere, or primitive shape that roughly matches its node’s visible content. For details on creating physics shapes, see [`SCNPhysicsShape`](scnphysicsshape.md).
- The [`kinematic()`](scnphysicsbody/kinematic().md) property. Applying a force or torque to a dynamic body results in an acceleration (or angular acceleration) proportional to its mass.

All values in SceneKit’s physics simulation use the International System of Units (SI): The unit of mass is the kilogram; the units of force, impulse, and torque are the newton, newton-second, and newton-meter; and the unit of distance for node positions and sizes is the meter. Note that you need not attempt to provide realistic values for physical quantities—use whatever values produce the behavior or gameplay you’re looking for.

For a dynamic body, you can control how the body is affected by forces or collisions. See Defining How Forces Affect a Physics Body.

##### Defining a Bodys Category and Collisions

When you design a game that uses physics, you define the different categories of physics objects that appear in the scene. You define different categories of physics bodies for the behaviors your want for your app. A body can be assigned to as many of these categories as you want. In addition to declaring its own categories, a physics body also declares which categories of bodies it interacts with.

Use the [`categoryBitMask`](scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) properties to define an object’s collision behavior. The constants listed in [`SCNPhysicsCollisionCategory`](scnphysicscollisioncategory.md) provide default values for these properties. In addition, with the [`contactTestBitMask`](scnphysicsbody/contacttestbitmask.md) property you can define interactions where a pair of bodies generates contact messages (see the [`SCNPhysicsContactDelegate`](scnphysicscontactdelegate.md) protocol) without the bodies being affected by the collision.

##### Related Physics Classes

Physics fields create forces that affect all bodies in an area, such as vortices and gravitational attraction. For details and a list of available field types, see [`SCNPhysicsField`](scnphysicsfield.md).

You can add higher-level behaviors that control interactions between multiple bodies, such as joints and wheeled vehicles. For details and a list of available behaviors, see [`SCNPhysicsBehavior`](scnphysicsbehavior.md).

A scene’s [`physicsWorld`](scnscene/physicsworld.md) property holds an [`SCNPhysicsWorld`](scnphysicsworld.md) object that manages physics characteristics that affect the entire scene.

##### Physics and the Rendering Loop

SceneKit evaluates its physics simulation as part of the rendering loop described in [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md). On each pass through this loop, SceneKit determines the state of all nodes with attached physics bodies, and simulates the effects of physics on those bodies for one time step—for example, by updating the position or rotation of a body based on its velocity and angular velocity. After simulating physics, SceneKit applies the results of the physics simulation to the scene for display.

Because you can animate SceneKit content not only through physics, but also through actions and implicitly and explicitly defined animations, SceneKit applies the results of physics simulation not to the [`SCNNode`](scnnode.md) objects in your scene, but to each node’s [`presentation`](scnnode/presentation.md) object that represents its currently displayed state. As such, changing properties of a node that are affected by physics  requires special consideration.

If you change the [`transform`](scnnode/transform.md) value—or any of the other properties that are components of the transform, such as [`position`](scnnode/position.md) and [`rotation`](scnnode/rotation.md)—of a node affected by physics, SceneKit resets the physics simulation for that node. If you want to change only one component of the transform, while leaving the others at their physics-simulated values, copy the presentation node’s transform before making changes, as shown below:

## Topics

### Creating Physics Bodies
- [convenience init(type: SCNPhysicsBodyType, shape: SCNPhysicsShape?)](scnphysicsbody/init(type:shape:).md)
  Creates a physics body with the specified type and shape.
- [class func `static`() -> Self](scnphysicsbody/static.md)
  Creates a physics body that is unaffected by forces or collisions and that cannot move.
- [class func dynamic() -> Self](scnphysicsbody/dynamic.md)
  Creates a physics body that can be affected by forces and collisions.
- [class func kinematic() -> Self](scnphysicsbody/kinematic.md)
  Creates a physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.
### Defining How Forces Affect a Physics Body
- [var physicsShape: SCNPhysicsShape?](scnphysicsbody/physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [var type: SCNPhysicsBodyType](scnphysicsbody/type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](scnphysicsbody/type.md) property and when creating a physics body.
- [var velocityFactor: SCNVector3](scnphysicsbody/velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var angularVelocityFactor: SCNVector3](scnphysicsbody/angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](scnphysicsbody/isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.
### Defining a Body’s Physical Properties
- [var mass: CGFloat](scnphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var charge: CGFloat](scnphysicsbody/charge.md)
  The electric charge of the body, in coulombs.
- [var friction: CGFloat](scnphysicsbody/friction.md)
  The body’s resistance to sliding motion.
- [var rollingFriction: CGFloat](scnphysicsbody/rollingfriction.md)
  The body’s resistance to rolling motion.
- [var restitution: CGFloat](scnphysicsbody/restitution.md)
  A factor that determines how much kinetic energy the body loses or gains in collisions.
- [var damping: CGFloat](scnphysicsbody/damping.md)
  A factor that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](scnphysicsbody/angulardamping.md)
  A factor that reduces the body’s angular velocity.
- [var momentOfInertia: SCNVector3](scnphysicsbody/momentofinertia.md)
  The body’s moment of inertia, expressed in the local coordinate system of the node that contains the body.
- [var usesDefaultMomentOfInertia: Bool](scnphysicsbody/usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.
- [var centerOfMassOffset: SCNVector3](scnphysicsbody/centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.
### Working with Contacts and Collisions
- [var categoryBitMask: Int](scnphysicsbody/categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var contactTestBitMask: Int](scnphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of bodies cause intersection notifications with this physics body.
- [var collisionBitMask: Int](scnphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [struct SCNPhysicsCollisionCategory](scnphysicscollisioncategory.md)
  Default values for a physics body’s [`categoryBitMask`](scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) properties.
- [var continuousCollisionDetectionThreshold: CGFloat](scnphysicsbody/continuouscollisiondetectionthreshold.md)
  The minimum distance the body must travel for SceneKit to apply a more precise (but more costly) algorithm to detect contacts with other bodies.
### Applying Forces, Impulses, and Torques
- [func applyForce(SCNVector3, asImpulse: Bool)](scnphysicsbody/applyforce(_:asimpulse:).md)
  Applies a force or impulse to the body at its center of mass.
- [func applyForce(SCNVector3, at: SCNVector3, asImpulse: Bool)](scnphysicsbody/applyforce(_:at:asimpulse:).md)
  Applies a force or impulse to the body at a specific point.
- [func applyTorque(SCNVector4, asImpulse: Bool)](scnphysicsbody/applytorque(_:asimpulse:).md)
  Applies a net torque or a change in angular momentum to the body.
- [func clearAllForces()](scnphysicsbody/clearallforces.md)
  Cancels all continuous forces and torques acting on the physics body during the current simulation step.
### Interacting with Bodies in Motion
- [var velocity: SCNVector3](scnphysicsbody/velocity.md)
  A vector describing both the current speed (in meters per second) and direction of motion of the physics body.
- [var angularVelocity: SCNVector4](scnphysicsbody/angularvelocity.md)
  A vector describing both the current rotation axis and rotational speed (in radians per second) of the physics body.
### Defining When a Body Can Move
- [var isResting: Bool](scnphysicsbody/isresting.md)
  A Boolean value that indicates whether the physics body is at rest.
- [var allowsResting: Bool](scnphysicsbody/allowsresting.md)
  A Boolean value that specifies whether SceneKit can automatically mark the physics body at rest.
- [func setResting(Bool)](scnphysicsbody/setresting(_:).md)
  Tells SceneKit whether to treat the body as currently being in motion.
### Synchronizing a Physics Body with its Node
- [func resetTransform()](scnphysicsbody/resettransform.md)
  Updates the position and orientation of a body in the physics simulation to match that of the node to which the body is attached.
### Instance Properties
- [var angularRestingThreshold: CGFloat](scnphysicsbody/angularrestingthreshold.md)
- [var linearRestingThreshold: CGFloat](scnphysicsbody/linearrestingthreshold.md)

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

- [class SCNPhysicsShape](scnphysicsshape.md)
  An abstraction of a physics body’s solid volume for tuning collision detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody)*