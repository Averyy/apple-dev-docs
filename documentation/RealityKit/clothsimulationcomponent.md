# ClothSimulationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that marks an entity as the simulation root of a localized cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothSimulationComponent
```

#### Overview

Each entity in a scene belongs to at most one cloth simulation, which is the ancestor closest in the entity hierarchy with a [`ClothSimulationComponent`](clothsimulationcomponent.md). Separate simulations do not interact with each other, which can improve power and performance. As an example, if you want two cloth simulations, then you can set up your entity hierarchy as follows.

```None
- scene
  - entity1 (ClothSimulationComponent)
    - entity2 (ClothBodyComponent)
  - entity3 (ClothSimulationComponent)
    - entity4 (ClothBodyComponent)
    - entity5
      - entity6 (ClothColliderComponent)
```

In the above example, `entity1` is the root of a cloth simulation and `entity2` is part of that simulation. Similarly, `entity3` is the root of a different cloth simulation that `entity4`, `entity5`, and `entity6` are all part of.

The simulation component itself mainly configures the quality, performance, and pace of the simulation. The solver and time step together balance the quality vs. performance of the simulation. You can guide the pace of the simulation by controlling its target clock ([`targetClock`](clothsimulationcomponent/targetclock.md)). Meanwhile, you can also follow the pace of the simulation by syncing with its simulation clock ([`simulationClock`](clothsimulationcomponent/simulationclock.md)).

The simulation component also stores various parameters that affect the entire simulation, like gravity. Notably, it stores the collection of runtime-modifiable materials that are available to its bodies ([`ClothBodyComponent`](clothbodycomponent.md)) and colliders ([`ClothColliderComponent`](clothcollidercomponent.md)). The exact interactions between these materials can be further configured through the simulation’s friction overrides.

## Topics

### Creating a cloth simulation
- [init(solver: ClothSimulationComponent.Solver)](clothsimulationcomponent/init(solver:).md)
  Creates a new simulation component for cloth bodies.
### Configuring the solver
- [var solver: ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.property.md)
  The solver used by this simulation, configured at initialization and immutable thereafter.
- [ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.struct.md)
  The permanent solver configuration of a cloth simulation.
### Applying forces
- [var gravity: SIMD3<Float>](clothsimulationcomponent/gravity.md)
  The gravitational acceleration for the bodies in the simulation, in m/s².
- [var wind: SIMD3<Float>](clothsimulationcomponent/wind.md)
  The wind force affecting all the cloth bodies in the simulation, in Newtons.
- [var dampingFactor: Float](clothsimulationcomponent/dampingfactor.md)
  The damping factor affecting all the cloth bodies in the simulation. The expected range is between 0 and 1 (included).
### Assigning materials
- [var materials: ClothSimulationComponent.MaterialCollection](clothsimulationcomponent/materials.md)
  A collection of materials that cloth colliders and cloth bodies can use in this simulation.
- [ClothSimulationComponent.MaterialCollection](clothsimulationcomponent/materialcollection.md)
  A collection of materials.
- [ClothSimulationComponent.Material](clothsimulationcomponent/material.md)
  A material that represents a cloth body or collider material.
### Overriding friction
- [var frictionOverrides: ClothSimulationComponent.FrictionOverridesCollection](clothsimulationcomponent/frictionoverrides.md)
  A map to manually override friction values between pairs of materials.
- [ClothSimulationComponent.FrictionOverridesCollection](clothsimulationcomponent/frictionoverridescollection.md)
  A collection of materials pairs whose combined frictions are overridden.
### Controlling simulation timing
- [var timeStep: Float](clothsimulationcomponent/timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](clothsimulationcomponent/meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.
### Synchronizing the clock
- [var targetClock: CMClockOrTimebase](clothsimulationcomponent/targetclock.md)
  The clock that this simulation attempts to follow.
- [var simulationClock: CMClockOrTimebase](clothsimulationcomponent/simulationclock.md)
  The clock that tracks the pace of this simulation.
### Initializers
- [init()](clothsimulationcomponent/init.md)
  Creates a new simulation component for cloth bodies.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent)*