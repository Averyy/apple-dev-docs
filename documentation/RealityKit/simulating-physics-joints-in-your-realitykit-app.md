# Simulating physics joints in your RealityKit app

**Framework**: RealityKit

Create realistic, connected motion using physics joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- Xcode 16.0+

#### Overview

This sample app demostrates how to create a [`PhysicsRevoluteJoint`](physicsrevolutejoint.md) that simulates motion, like a pendulum swinging back and forth, as an alternative to animations.

You can create animations to depict objects in motion but simulations can be better for more complicated scenes because they can work with more variables, and support custom motion that react dynamically to external factors, such as a person’s gestures.

> **Note**: All joint types in RealityKit conform to the [`PhysicsJoint`](physicsjoint.md) protocol, including [`PhysicsRevoluteJoint`](physicsrevolutejoint.md).

All joint types in RealityKit conform to the [`PhysicsJoint`](physicsjoint.md) protocol, including [`PhysicsRevoluteJoint`](physicsrevolutejoint.md).

##### Set Up the Apps Static Scene

##### Add Physics Components to the Entities

Before you activate a physics joint, each entity must have both a [`PhysicsBodyComponent`](physicsbodycomponent.md) and a [`CollisionComponent`](collisioncomponent.md).

This app adds a physics body and collision shape that matches the model’s spherical shape, where `pendulumSettings.ballRadius` characterizes its radius.

To respond to forces like gravity and collisions, set the ball’s [`mode`](physicsbodycomponent/mode.md) to [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md). Set its material to have no friction and a restitution of `1`, to result in completely elastic collisions:

```swift
let collisionShape = ShapeResource.generateSphere(
    radius: pendulumSettings.ballRadius)

var ballBody = PhysicsBodyComponent(
    shapes: [collisionShape],
    mass: pendulumSettings.ballMass,
    material: .generate(staticFriction: 0, dynamicFriction: 0, restitution: 1),
    mode: .dynamic
)
ballBody.linearDamping = 0
let ballCollision = CollisionComponent(shapes: [ballShape])

ballEntity.components.set([ballBody, ballCollision])
```

Because other forces can’t move the other end of the physics joint (`attachmentEntity`), set its [`mode`](physicsbodycomponent/mode.md) to [`PhysicsBodyMode.static`](physicsbodymode/static.md):

```swift
let attachmentShape = ShapeResource.generateBox(
    size: pendulumSettings.attachmentSize * pendulumSettings.ballRadius
)

var attachmentBody = PhysicsBodyComponent(
    shapes: [attachmentShape], mass: 1,
    material: .generate(staticFriction: 0, dynamicFriction: 0, restitution: 1),
    mode: .static
)
attachmentBody.linearDamping = 0
let attachmentCollision = CollisionComponent(shapes: [attachmentShape])

attachmentEntity.components.set([attachmentBody, attachmentCollision])
```

##### Add the Simulation and Physics Joints Components

The app adds the components [`PhysicsSimulationComponent`](physicssimulationcomponent.md) and [`PhysicsJointsComponent`](physicsjointscomponent.md) to a common ancestor of `ballEntity` and `attachmentEntity`, to indicate where RealityKit adds the joints:

```swift
// Add physics simulation component to parent simulation entity.
parentSimulationEntity.components.set(PhysicsSimulationComponent())
// Add physics joints component to parent simulation entity.
parentSimulationEntity.components.set(PhysicsJointsComponent())
```

##### Create a New Joint

[`PhysicsRevoluteJoint`](physicsrevolutejoint.md) creates a hinge for the swinging motion in this example. A revolute joint, also known as a , allows rotational movement in one axis, similar to a door swinging on its hinges.

> **Note**: [`PhysicsRevoluteJoint`](physicsrevolutejoint.md) conforms to [`PhysicsJoint`](physicsjoint.md), a protocol for all physics joints.

[`PhysicsRevoluteJoint`](physicsrevolutejoint.md) conforms to [`PhysicsJoint`](physicsjoint.md), a protocol for all physics joints.

A joint needs two [`GeometricPin`](geometricpin.md) instances on separate entities to create a physics joint.

The app creates each pin with the method [`set(named:position:orientation:)`](entitygeometricpins/set(named:position:orientation:).md) on its respective entity. Use [`pins`](entity/pins.md) to access all pins an entity owns:

```swift
// Rotate hinge orientation from x to z-axis.
let hingeOrientation = simd_quatf(from: [1, 0, 0], to: [0, 0, 1])

// The attachment's pin is in the center of
// the attachment entity.
let attachmentPin = attachmentEntity.pins.set(
    named: "attachment_hinge",
    position: .zero,
    orientation: hingeOrientation
)

// The ball's pin is at the center of the
// attachment entity in local space.
let relativeJointLocation = attachmentEntity.position(
    relativeTo: ballEntity
)

let ballPin = ballEntity.pins.set(
    named: "ball_hinge",
    position: relativeJointLocation,
    orientation: hingeOrientation
)
```

> 💡 **Tip**: [`PhysicsRevoluteJoint`](physicsrevolutejoint.md) always rotates around the pins’ local x-axis, but in this example the models rotate around the z-axis because the variable `hingeOrientation` realigns the pins’ x-axis (`[1, 0, 0]`) to the z-axis (`[0, 0, 1]`).

[`PhysicsRevoluteJoint`](physicsrevolutejoint.md) always rotates around the pins’ local x-axis, but in this example the models rotate around the z-axis because the variable `hingeOrientation` realigns the pins’ x-axis (`[1, 0, 0]`) to the z-axis (`[0, 0, 1]`).

Use each [`GeometricPin`](geometricpin.md) as the parameters to create a new [`PhysicsRevoluteJoint`](physicsrevolutejoint.md):

```swift
let revoluteJoint = PhysicsRevoluteJoint(pin0: attachmentPin, pin1: ballPin)
```

##### Add the Physics Joint to Your Simulation

Add the new joint to the simulation. The [`addToSimulation()`](physicsjoint/addtosimulation().md) method finds the closest entity ancestor of the joint’s first pin that has a [`PhysicsJointsComponent`](physicsjointscomponent.md), and adds the joint to its [`joints`](physicsjointscomponent/joints.md) collection:

```swift
try revoluteJoint.addToSimulation()
```

##### Add Motion to the Scene

The simulation shows no effect until you add motion. One way to do so is via [`ImpulseAction`](impulseaction.md). Give the ball a push in the negative x-direction to start the simulation:

```swift
let impulseAction = ImpulseAction(
    targetEntity: .sourceEntity,
    linearImpulse: pendulumSettings.impulsePower)
let impulseAnimation = try AnimationResource.makeActionAnimation(
    for: impulseAction)

ballEntity.playAnimation(impulseAnimation)
```

The following video shows the resulting scene, with the `ballEntity` swinging left and right on the hinge:

In the sample app, you can change the static value `PendulumSettings.pendulumCount` to a larger number such as `5` to place multiple pendulums in the app, and see them collide with each other:

## See Also

- [struct GeometricPin](geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [struct GeometricPinsComponent](geometricpinscomponent.md)
  A component that stores a sequence of geometric pins.
- [protocol PhysicsJoint](physicsjoint.md)
  A type that describes physics joints.
- [struct PhysicsJointsComponent](physicsjointscomponent.md)
  A component that stores physics joints which RealityKit simulates.
- [struct EntityGeometricPins](entitygeometricpins.md)
  A structure that wraps all geometric pins an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simulating-physics-joints-in-your-realitykit-app)*