# Physics joints and pins

**Framework**: RealityKit

Simulate joint physics that connect virtual objects.

#### Overview

In a 3D environment, you can animate various attributes of an [`Entity`](entity.md) such as its location, rotation, and size from one value to another. This is ideal for simple pre-defined motion, but does not allow for interaction with external forces, such as collisions with other objects, or gestures. With a [`PhysicsJoint`](physicsjoint.md) you can connect entities with pins, and RealityKit keeps your entities bound by constraints that you define.

Each joint consists of two pins, each of which belongs to a different entity. Each [`GeometricPin`](geometricpin.md) moves and rotates relative to each other within the bounds of the joint’s constraints.

## Topics

### Pin and joint components
- [Simulating physics joints in your RealityKit app](simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
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
### Built-in joint types
- [struct PhysicsRevoluteJoint](physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
- [struct PhysicsPrismaticJoint](physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsSphericalJoint](physicssphericaljoint.md)
  A spherical joint that allows free rotational movement between two entities’ pins.
- [struct PhysicsCustomJoint](physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.

## See Also

- [Collision detection](physics-collision-detection.md)
  Determine when entities collide with each other or the environment.
- [Simulations and motion](physics-simulations-and-motion.md)
  Simulate physical interactions between entities or systems.
- [Force effects](physics-force-effects.md)
  Control the movement of virtual objects with forces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physics-joints-and-pins)*