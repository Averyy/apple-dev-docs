# Cloth simulation

**Framework**: RealityKit

Add fabric, soft surfaces, and draping materials that bend, fold, and respond to forces and contact in your 3D scenes.

#### Overview

This collection covers the components, shapes, and resources you use to add simulated fabric and other deformable surfaces to a scene. Use it to give an entity cloth-like behavior, define its physical material and shape, and control how it collides with the world around it. You can shape how the simulation responds to forces, grabbing, and query regions, and react to the events it generates as it runs. Reach for these APIs when static or rigid-body geometry can’t capture the flowing, draping motion you want.

## Topics

### Simulation and bodies
- [struct ClothSimulationComponent](clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyComponent](clothbodycomponent.md)
  A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.
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
### Cloth shapes
- [struct ClothMeshShape](clothmeshshape.md)
  Shape representing a mesh with a configurable inflation bias.
- [struct ClothPlaneShape](clothplaneshape.md)
  Shape representing an infinite plane that encloses one half of the world.
- [struct ClothBoxShape](clothboxshape.md)
  Shape representing a box.
- [struct ClothRoundedBoxShape](clothroundedboxshape.md)
  Shape representing a box with rounded edges.
- [struct ClothSphereShape](clothsphereshape.md)
  Shape representing a sphere.
- [struct ClothCapsuleShape](clothcapsuleshape.md)
  Shape representing a capsule (full height is `height + 2 * radius`).
- [enum ClothVolumeShape](clothvolumeshape.md)
  Shape suitable for use as a volume.
### Collision
- [struct ClothColliderComponent](clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [enum ClothColliderShape](clothcollidershape.md)
  Shape suitable for use as a collider.
- [struct ClothColliderMaterial](clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionFilter](clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.
- [struct ClothCollisionGroupSet](clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.
### Cloth events
- [enum ClothSimulationEvents](clothsimulationevents.md)
  Types of events that a cloth simulation publishes during its lifetime.
- [enum ClothBodyEvents](clothbodyevents.md)
  Types of events that a cloth body publishes during its lifetime.
- [enum ClothColliderEvents](clothcolliderevents.md)
  Types of events that a cloth collider publishes during its lifetime.
- [enum ClothQueryVolumeEvents](clothqueryvolumeevents.md)
  Types of events that a cloth query volume publishes during its lifetime.
### Cloth resources
- [class ClothMeshResource](clothmeshresource.md)
  A mesh resource that defines the topology and shape of a cloth body or a mesh-shaped cloth collider.
- [class ClothPoseResource](clothposeresource.md)
  A resource that defines a set of vertex positions for a cloth body.

## See Also

- [Collision detection](physics-collision-detection.md)
  Determine when entities collide with each other or the environment.
- [Simulations and motion](physics-simulations-and-motion.md)
  Simulate physical interactions between entities or systems.
- [Force effects](physics-force-effects.md)
  Control the movement of virtual objects with forces.
- [Physics joints and pins](physics-joints-and-pins.md)
  Simulate joint physics that connect virtual objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physics-cloth-simulation)*