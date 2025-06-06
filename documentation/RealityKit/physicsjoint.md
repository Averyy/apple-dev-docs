# PhysicsJoint

**Framework**: RealityKit  
**Kind**: protocol

A type that describes physics joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PhysicsJoint : Equatable
```

#### Overview

`PhysicsJoint` objects are transient and define physics joints properties. [`PhysicsJointsComponent`](physicsjointscomponent.md) stores physics joints when added to an entity.

Each `PhysicsJoint` references two entities at local poses (position and orientation) specified on each [`Entity`](entity.md).

The two pins of a physics joint, [`pin0`](physicsjoint/pin0.md) and [`pin1`](physicsjoint/pin1.md), each reference poses on the entities that make up each point on a `PhysicsJoint`. Use two unique entities that both have a [`PhysicsBodyComponent`](physicsbodycomponent.md), and belong to the same physics simulation.

Joints specify linear and angular limits of motion, limiting the motion of the second pin ([`pin1`](physicsjoint/pin1.md)) relative to the first pin ([`pin0`](physicsjoint/pin0.md)).

To become active, the `PhysicsJoint` needs to be added to a [`PhysicsJointsComponent`](physicsjointscomponent.md)  This is achieved by either directly on the component, or by calling [`addToSimulation()`](physicsjoint/addtosimulation().md). Once you add the joint to the simulation context, you no longer need to reference `PhysicsJoint` directly in your code.

For example, a [`PhysicsRevoluteJoint`](physicsrevolutejoint.md) that connects a window, `windowEntity`, to a window frame, `frameEntity`:

```swift
let parentSimulationEntity = Entity()
// Add PhysicsSimulationComponent to parentSimulationEntity...

let frameEntity = Entity()
let windowEntity = Entity()
// Add PhysicsBodyComponents to the entities...

// Create a hinge the references points on the entities.
let windowWidth: Float = 1
let framePin = frameEntity.pins.set(
    named: "FrameHinge",
    // In this example, center of the frame is the center of its bounding box,
    // so the hinge is half its width to the negative x direction.
    position: [-windowWidth / 2, 0, 0],
    // This hinge rotates around the x-axis, but this window needs to
    // rotate around the y-axis.
    // This rotation modifies the pin's positive x-axis to the positive y-axis.
    orientation: simd_quatf(from: [1, 0, 0], to: [0, 1, 0])
)

// Get a previously created GeometricPin from `windowEntity`,
// or a new one create one as above.
let windowPin = GeometricPin(entity: windowEntity, pinName: "WindowHinge")

let windowHingeJoint = PhysicsRevoluteJoint(
    pin0: framePin,
    pin1: windowPin,
    // Allow the hinge to rotate up to 90º.
    angularLimit: 0...Float.pi
)
try windowHingeJoint.addToSimulation()
```

- When creating a joint, make sure that the jointed entities are initially positioned so that they satisfy the joint. If not done so, the physics solver may have difficulty bringing the entities together to satisfy the joint.
- When connecting a [`PhysicsBodyMode.kinematic`](physicsbodymode/kinematic.md) and a [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md) entities by a joint, use [`pin0`](physicsjoint/pin0.md) as the pin on the kinematic entity.
If both are [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md), set the heavier entity as [`pin0`](physicsjoint/pin0.md).
- Aim to make the entities connected by joints similar in mass.
- Add a [`PhysicsSimulationComponent`](physicssimulationcomponent.md) to a common ancestor when creating `PhysicsJoint` instances, to make it clear which physics simulation is used to solve the joints.
- To improve the the solving of the joints, adjust the value of the [`solverIterations`](physicssimulationcomponent/solveriterations-swift.property.md) property.

## Topics

### Instance Properties
- [var checksForInternalCollisions: Bool](physicsjoint/checksforinternalcollisions.md)
  A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.
- [var isActive: Bool](physicsjoint/isactive.md)
  A Boolean that indicates whether the joint is active.
- [var pin0: GeometricPin](physicsjoint/pin0.md)
  The pin that defines a local position and orientation on the first entity.
- [var pin1: GeometricPin](physicsjoint/pin1.md)
  The pin that defines a local position and orientation on the second entity.
### Instance Methods
- [func addToSimulation() throws -> Entity](physicsjoint/addtosimulation.md)
  Adds this joint to the simulation.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
### Conforming Types
- [PhysicsCustomJoint](physicscustomjoint.md)
- [PhysicsDistanceJoint](physicsdistancejoint.md)
- [PhysicsFixedJoint](physicsfixedjoint.md)
- [PhysicsPrismaticJoint](physicsprismaticjoint.md)
- [PhysicsRevoluteJoint](physicsrevolutejoint.md)
- [PhysicsSphericalJoint](physicssphericaljoint.md)

## See Also

- [Simulating physics joints in your RealityKit app](simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
- [struct GeometricPin](geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [struct GeometricPinsComponent](geometricpinscomponent.md)
  A component that stores a sequence of geometric pins.
- [struct PhysicsJointsComponent](physicsjointscomponent.md)
  A component that stores physics joints which RealityKit simulates.
- [struct EntityGeometricPins](entitygeometricpins.md)
  A structure that wraps all geometric pins an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoint)*