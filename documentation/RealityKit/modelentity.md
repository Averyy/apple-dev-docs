# ModelEntity

**Framework**: RealityKit  
**Kind**: class

A representation of a physical object that RealityKit renders and optionally simulates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class ModelEntity
```

## Mentions

- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Loading entities from a file](loading-entities-from-a-file.md)

#### Overview

Use one or more model entities to place physical objects in a scene. In addition to the components they inherit from the [`Entity`](entity.md) class, model entities have geometry, described by their [`ModelComponent`](modelcomponent.md). Model entities acquire the model component by conforming to the [`HasModel`](hasmodel.md) protocol. You specify meshes and materials to control how a model entity appears.

![Diagram showing the components present in the model](https://docs-assets.developer.apple.com/published/4fd5262b43f0c873c7625b95738c59a5/ModelEntity-1%402x.png)

Models respond to physics simulations because they conform to the [`HasPhysics`](hasphysics.md) protocol. You give them mass and other physical properties with a [`PhysicsBodyComponent`](physicsbodycomponent.md) instance, and then apply forces or impulses. The simulator uses a [`PhysicsMotionComponent`](physicsmotioncomponent.md) to manage the linear and angular velocity of the object. Alternatively, you can selectively circumvent the simulation to control position and velocity yourself. Do this for a given model by setting its physics body [`mode`](physicsbodycomponent/mode.md) to [`PhysicsBodyMode.kinematic`](physicsbodymode/kinematic.md).

Models can also collide with one another, and with other entities that conform to the [`HasCollision`](hascollision.md) protocol. The [`CollisionComponent`](collisioncomponent.md) provides parameters that let you manage which models collide with each other. It also lets you control the collision shape, which for performance reasons, is typically simpler than the visual geometry.

## Topics

### Creating a model
- [init()](modelentity/init.md)
  Creates a model entity.
- [init(mesh: MeshResource, materials: [any Material])](modelentity/init(mesh:materials:).md)
  Creates a model entity with a particular mesh and set of materials.
- [init(mesh: MeshResource, materials: [any Material], collisionShape: ShapeResource, mass: Float)](modelentity/init(mesh:materials:collisionshape:mass:).md)
  Creates a model entity with a particular mesh, set of materials, collision shape, and mass.
- [init(mesh: MeshResource, materials: [any Material], collisionShapes: [ShapeResource], mass: Float)](modelentity/init(mesh:materials:collisionshapes:mass:).md)
  Creates a model entity with a particular mesh, set of materials, a composite collision shape, and mass.
### Configuring the model
- [var model: ModelComponent?](modelentity/model.md)
  The model component for the entity.
- [var jointNames: [String]](modelentity/jointnames.md)
  The names of all the joints in the model entity.
- [var jointTransforms: [Transform]](modelentity/jointtransforms.md)
  The relative joint transforms of the model entity.
### Detecting collisions
- [var collision: CollisionComponent?](modelentity/collision.md)
  The collision component that gives the entity the ability to participate in collision simulations.
### Simulating forces, impulses, and motion
- [var physicsBody: PhysicsBodyComponent?](modelentity/physicsbody.md)
  A component that is used for physics simulations of the model entity in accordance with the laws of Newtonian mechanics.
- [var physicsMotion: PhysicsMotionComponent?](modelentity/physicsmotion.md)
  The physics motion component used by physics simulations of the model entity.
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:relativeto:).md)
  Applies a force to the physics body at its center of mass.
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:at:relativeto:).md)
  Applies a force to the physics body at the specified position.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](modelentity/addtorque(_:relativeto:).md)
  Applies a torque to the physics body at its center of mass.
- [func clearForcesAndTorques()](modelentity/clearforcesandtorques.md)
  Clears all forces previously added to the physics body.
- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applylinearimpulse(_:relativeto:).md)
  Applies an impulse to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.
- [func resetPhysicsTransform(recursive: Bool)](modelentity/resetphysicstransform(recursive:).md)
  Resets the position, orientation, and velocities of the simulated physics body.
- [func resetPhysicsTransform(Transform, recursive: Bool)](modelentity/resetphysicstransform(_:recursive:).md)
  Resets the position and velocities of the simulated physics body.
### Default Implementations
- [HasCollision Implementations](modelentity/hascollision-implementations.md)
- [HasModel Implementations](modelentity/hasmodel-implementations.md)
- [HasPhysicsBody Implementations](modelentity/hasphysicsbody-implementations.md)
- [HasPhysicsMotion Implementations](modelentity/hasphysicsmotion-implementations.md)

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasCollision](hascollision.md)
- [HasHierarchy](hashierarchy.md)
- [HasModel](hasmodel.md)
- [HasPhysics](hasphysics.md)
- [HasPhysicsBody](hasphysicsbody.md)
- [HasPhysicsMotion](hasphysicsmotion.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class MeshResource](meshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity)*