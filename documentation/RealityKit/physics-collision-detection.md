# Collision detection

**Framework**: RealityKit

Determine when entities collide with each other or the environment.

#### Overview

RealityKit can automatically detect when two objects participating in the physics system collide with each other if both entities have a [`CollisionComponent`](collisioncomponent.md) with at least one . Because doing collision detection with complex 3D models can be computationally expensive, collision shapes are simpler, invisible shapes RealityKit uses to detect collision, as well as doing hit testing, ray casts, and convex shape casts.

Entities can participate in the scene simulation in two different modes: as a  or as a . A rigid body fully participates in the collision simulation. It affects the velocity and direction of other rigid body entities with which it collides. An entity with a rigid body [`mode`](physicsbodycomponent/mode.md) of [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md), other rigid body entities can affect its velocity and direction. A trigger entity doesn’t have any impact on the other rigid bodies in the scene, but can trigger code or Reality Composer Pro behaviors when another rigid body entity overlaps it.

Turn an entity into a trigger by adding a [`CollisionComponent`](collisioncomponent.md) to it and setting its [`mode`](collisioncomponent/mode-swift.property.md) to [`CollisionComponent.Mode.trigger`](collisioncomponent/mode-swift.enum/trigger.md).

Turn an entity into a  by adding a [`PhysicsBodyComponent`](physicsbodycomponent.md) to the entity in addition to a [`CollisionComponent`](collisioncomponent.md). The [`PhysicsBodyComponent`](physicsbodycomponent.md) defines the physical properties of the entity, such as its mass and collision shape.

> **Note**: RealityKit ignores an entity’s collision component mode if the entity also has a [`PhysicsBodyComponent`](physicsbodycomponent.md). An entity can be a rigid body, or a trigger, but not both at the same time.

## Topics

### Collision shapes and groups
- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [struct CollisionComponent](collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [CollisionComponent.Mode](collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.
- [class ShapeResource](shaperesource.md)
  A representation of a shape.
- [enum ShapeResourceError](shaperesourceerror.md)
- [struct CollisionGroup](collisiongroup.md)
  A bitmask used to define the collision group to which an entity belongs.
- [struct CollisionFilter](collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.
- [class TriggerVolume](triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.
### Collision-related notifications
- [enum CollisionEvents](collisionevents.md)
- [struct Contact](contact.md)
  Events associated with collisions.
### Ray casting
- [struct CollisionCastHit](collisioncasthit.md)
  A hit result of a collision cast.
- [enum CollisionCastQueryType](collisioncastquerytype.md)
  The kinds of ray and convex shape cast queries that you can make.
- [struct PixelCastHit](pixelcasthit.md)
### Entity compliance
- [protocol HasCollision](hascollision.md)
  An interface used for ray casting and collision detection.

## See Also

- [Simulations and motion](physics-simulations-and-motion.md)
  Simulate physical interactions between entities or systems.
- [Force effects](physics-force-effects.md)
  Control the movement of virtual objects with forces.
- [Physics joints and pins](physics-joints-and-pins.md)
  Simulate joint physics that connect virtual objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physics-collision-detection)*