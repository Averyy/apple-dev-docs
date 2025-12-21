# ModelEntity

**Framework**: RealityKit  
**Kind**: class

A representation of a physical object that RealityKit renders and optionally simulates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class ModelEntity
```

## Mentions

- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
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

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
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
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class MeshResource](meshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity)*