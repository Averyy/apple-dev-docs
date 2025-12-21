# CollisionComponent

**Framework**: RealityKit  
**Kind**: struct

A component that gives an entity the ability to collide with other entities that also have collision components.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct CollisionComponent
```

#### Overview

This component holds the entity’s data related to participating in the scene’s physics simulation. It is also used to calculate collision queries, raycasts, and convex shape casts. Entities can participate in the scene simulation in two different modes: as a  or as a .  A rigid body fully participates in the collision simulation. It affects the velocity and direction of entities it collides. If configured with a rigid body [`mode`](physicsbodycomponent/mode.md) of [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md), it’s own velocity and direction can be affected by other rigid body entities. A trigger entity doesn’t have any impact on the rigid bodies in the scene, but can trigger code or Reality Composer behaviors when a rigid body entity overlaps it.

Note the following when considering applying a non-uniform scale to an entity:

- Non-uniform scaling is applicable only to box, convex mesh and triangle mesh collision shapes.
- Non-uniform scaling is not supported for all other types of collision shapes. In this case the scale.x value is duplicated to the scale’s y and z components as well to force scale uniformity based on the x component.
- If the entity has a non-uniform scale assigned to its transform then that entity should not have any descendants assigned that contain rotations in their transforms. A good rule of thumb is to assign the non-uniform scale to the entity that has the collision shape, and avoid adding children below that entity.

Turn an entity into a trigger by adding a [`CollisionComponent`](collisioncomponent.md) to it and setting its [`mode`](collisioncomponent/mode-swift.property.md) to [`CollisionComponent.Mode.trigger`](collisioncomponent/mode-swift.enum/trigger.md).

Turn an entity into a  by adding a  [`PhysicsBodyComponent`](physicsbodycomponent.md) to the entity in addition to a [`CollisionComponent`](collisioncomponent.md).  The [`PhysicsBodyComponent`](physicsbodycomponent.md) defines the physical properties of the entity, such as its mass and collision shape.

The `filter` property defines the entity’s collision filter, which determines which other objects the entity collides with. For more information, see [`Controlling Entity Collisions in RealityKit`](controlling_entity_collisions_in_realitykit.md).

> **Note**: If an entity has a [`PhysicsBodyComponent`](physicsbodycomponent.md), the  collision component’s mode is ignored. An entity can be a rigid body, or a trigger, but not both at the same time.

## Topics

### Creating the collision component
- [init(shapes: [ShapeResource], mode: CollisionComponent.Mode, filter: CollisionFilter)](collisioncomponent/init(shapes:mode:filter:).md)
  Creates a collision component with the given collision shape, mode, and filter parameters.
### Setting the collision mode
- [var mode: CollisionComponent.Mode](collisioncomponent/mode-swift.property.md)
  The collision mode.
### Filtering collisions
- [var filter: CollisionFilter](collisioncomponent/filter.md)
  The collision filter used to segregate entities into different collision groups.
### Setting collision shapes
- [var shapes: [ShapeResource]](collisioncomponent/shapes.md)
  A collection of shape resources that collectively represent the outer dimensions of an entity for the purposes of collision detection.
### Structures
- [CollisionComponent.CollisionOptions](collisioncomponent/collisionoptions-swift.struct.md)
  The options set that defines how a collision object reports collisions.
### Initializers
- [init(shapes: [ShapeResource], isStatic: Bool, filter: CollisionFilter)](collisioncomponent/init(shapes:isstatic:filter:).md)
  Creates a collision component.
- [init(shapes: [ShapeResource], mode: CollisionComponent.Mode, collisionOptions: CollisionComponent.CollisionOptions, filter: CollisionFilter)](collisioncomponent/init(shapes:mode:collisionoptions:filter:).md)
### Instance Properties
- [var collisionOptions: CollisionComponent.CollisionOptions](collisioncomponent/collisionoptions-swift.property.md)
- [var isStatic: Bool](collisioncomponent/isstatic.md)
  A Boolean value that indicates whether the collider is static.
### Enumerations
- [CollisionComponent.Mode](collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncomponent)*