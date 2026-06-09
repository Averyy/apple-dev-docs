# ClothBodyComponent

**Framework**: RealityKit  
**Kind**: struct

A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothBodyComponent
```

#### Overview

A cloth body belongs to the simulation root defined by its closest ancestor entity with a [`ClothSimulationComponent`](clothsimulationcomponent.md), if any.

If the same entity has a [`ModelComponent`](modelcomponent.md), then the mesh of that component will follow the deformation of this cloth body. As an example, you can simulate and render a cloth body by setting up your entity hierarchy as follows.

```None
- scene
  - entity1 (ClothSimulationComponent)
    - entity2 (ClothBodyComponent + ModelComponent)
```

The simulated cloth body is effectively a deforming copy of the input mesh ([`ClothMeshResource`](clothmeshresource.md)) that it is initialized from. This mesh is known as the simulation mesh (also known as proxy mesh) of the body, and RealityKit does not render this mesh. In contrast, the mesh of the [`ModelComponent`](modelcomponent.md) is rendered and is known as the visual mesh of the cloth body in this context. Unless the mesh stored in the [`ModelComponent`](modelcomponent.md) is a [`LowLevelMesh`](lowlevelmesh.md), it will follow the deformation of the simulation mesh.

The simulation mesh can be the same as the visual mesh, but it is recommended to use a separate mesh. This is because there are quality and performance aspects to consider when picking a suitable simulation mesh. See [`mesh`](clothbodycomponent/mesh.md) for details.

A cloth body is effectively simulated as a cluster of constrained particles with different physical properties. Consequently, the vertices of the simulation mesh are sometimes referred to as particles.

## Topics

### Creating a cloth body
- [init(mesh: ClothMeshResource, meshDraping: ClothPoseResource?)](clothbodycomponent/init(mesh:meshdraping:).md)
  Creates a new cloth body component.
- [var mesh: ClothMeshResource](clothbodycomponent/mesh.md)
  The (simulation) mesh of the cloth body that defines the rest pose of the body.
- [var initialMeshDraping: ClothPoseResource?](clothbodycomponent/initialmeshdraping.md)
  An optional pose that specifies an already draped configuration of the cloth at the start of the simulation.
### Mapping the visual mesh
- [var visualMesh: LowLevelMesh?](clothbodycomponent/visualmesh.md)
  The dynamically deforming visual mesh of the cloth body, which you may read but not modify.
- [var visualMeshWeights: PerClothVertexData<Float>?](clothbodycomponent/visualmeshweights.md)
  Optional weights by which the visual mesh should be deformed according to the simulation mesh.
- [var materialNames: [String]](clothbodycomponent/materialnames.md)
  The names of the body materials used by this cloth body.
- [ClothBodyComponent.PerVisualVertexData](clothbodycomponent/pervisualvertexdata.md)
  Stores per-vertex data for all visual vertices in a buffer.
- [ClothBodyComponent.PerSimulationVertexData](clothbodycomponent/persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.
### Controlling cloth motion
- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](clothbodycomponent/motiontypes.md)
  Motion types for each particle in the body.
- [ClothBodyComponent.ParticleMotionType](clothbodycomponent/particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [var mass: Float](clothbodycomponent/mass.md)
  Mass of the body as a whole, in Kg.
- [static func resetDeformation(entity: Entity)](clothbodycomponent/resetdeformation(entity:).md)
  Resets the deformation of the cloth body to its initial pose and motion.
### Defining target shapes
- [var targetShapes: [ClothBodyComponent.TargetShape]](clothbodycomponent/targetshapes.md)
  The target shapes associated with the body.
- [ClothBodyComponent.TargetShape](clothbodycomponent/targetshape.md)
  Pulls particles of a cloth body toward positions in either local or simulation space.
### Applying external forces
- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](clothbodycomponent/externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [ClothBodyComponent.ExternalForce](clothbodycomponent/externalforce.md)
  An external force applied to a single particle, in Newtons.
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](clothbodycomponent/inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).
- [ClothBodyComponent.InflationConstraint](clothbodycomponent/inflationconstraint-swift.struct.md)
  Configuration for an inflatable cloth body.
### Managing collisions
- [var colliderBinding: ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md).
- [ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](clothbodycomponent/collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/enablecollisions(towards:).md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/disablecollisions(towards:).md)
  Disables one-way collisions towards the selected groups for all particles in the body.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ClothSimulationComponent](clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyMaterial](clothbodymaterial.md)
  A struct that represents a cloth body’s material.
- [struct ClothGrabComponent](clothgrabcomponent.md)
  A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.
- [struct ClothForceVolumeComponent](clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent)*