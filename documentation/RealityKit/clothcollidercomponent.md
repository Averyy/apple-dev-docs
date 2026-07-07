# ClothColliderComponent

**Framework**: RealityKit  
**Kind**: struct

A component that adds a cloth-compatible collider to an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothColliderComponent
```

#### Overview

A cloth collider belongs to the simulation root defined by its closest ancestor entity with a [`ClothSimulationComponent`](clothsimulationcomponent.md), if any.

By default, a collider ensures that cloth bodies ([`ClothBodyComponent`](clothbodycomponent.md)) stay outside of its shape. Colliders can also report when such collisions occur. Colliders themselves are not simulated and are (unlike bodies) not affected by bodies or by other colliders.

As an example, you can simulate and render a cloth body together with a collider by setting up your entity hierarchy as follows.

```None
- scene
  - rootEntity (ClothSimulationComponent)
    - dressEntity (ClothBodyComponent + ModelComponent)
    - characterEntity (ClothColliderComponent + ModelComponent)
```

The shape of a collider can either be a mesh or an implicit shape. All implicit shapes are mutable at runtime. The mesh shape is directly mutable at runtime only if it is a [`LowLevelMesh`](lowlevelmesh.md). When suitable, it is recommended to use colliders with implicit shapes for improved performance.

If the shape of a collider is a mesh and the same entity has a [`ModelComponent`](modelcomponent.md), then the two meshes will attempt to stay in sync. In this context, the mesh of the collider and the [`ModelComponent`](modelcomponent.md) would be known as the simulation mesh and visual mesh, respectively. In particular:

- if both meshes are [`LowLevelMesh`](lowlevelmesh.md), then they will not stay in sync at all.
- if only the simulation mesh is a [`LowLevelMesh`](lowlevelmesh.md), then the visual mesh will follow the simulation mesh.
- otherwise, the simulation mesh will follow the visual mesh (regardless if it is a [`LowLevelMesh`](lowlevelmesh.md)).

## Topics

### Creating a cloth collider
- [init(shape: ClothColliderShape)](clothcollidercomponent/init(shape:).md)
  Creates a cloth collider component with the given shape.
- [init(mesh: ClothMeshResource, bias: Float)](clothcollidercomponent/init(mesh:bias:).md)
  Creates a cloth collider component with a mesh shape built from the given mesh resource.
- [init(meshShape: ClothMeshShape)](clothcollidercomponent/init(meshshape:).md)
  Creates a cloth collider component with the given mesh shape.
### Configuring the collider shape
- [var shape: ClothColliderShape](clothcollidercomponent/shape.md)
  The (simulation) shape of the collider.
- [var materialNames: [String]](clothcollidercomponent/materialnames.md)
  The names of the collider materials used by this collider.
### Managing collision response
- [var isCollisionResponseEnabled: Bool](clothcollidercomponent/iscollisionresponseenabled.md)
  Indicates whether this collider pushes away intersecting cloth body particles.
- [func enableCollisions(towards: ClothCollisionGroupSet)](clothcollidercomponent/enablecollisions(towards:).md)
  Enables one-way collisions towards the selected groups.
- [func disableCollisions(towards: ClothCollisionGroupSet)](clothcollidercomponent/disablecollisions(towards:).md)
  Disables one-way collisions towards the selected groups.
### Instance Properties
- [var collisionFilter: ClothCollisionFilter](clothcollidercomponent/collisionfilter.md)
  Defines the collision groups that the collider belongs to, and the mask used to determine which groups this collider affects.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [enum ClothColliderShape](clothcollidershape.md)
  Shape suitable for use as a collider.
- [struct ClothColliderMaterial](clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionFilter](clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.
- [struct ClothCollisionGroupSet](clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent)*