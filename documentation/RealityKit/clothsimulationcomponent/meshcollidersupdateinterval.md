# meshCollidersUpdateInterval

**Framework**: RealityKit  
**Kind**: property

The number of time steps between updates to the mesh colliders in the simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var meshCollidersUpdateInterval: Int { get set }
```

#### Discussion

In this context, a mesh collider update is referring to when the collider applies and detects collisions. A higher interval results in worse collision detection but better performance and power.

The mesh colliders are guaranteed to update on the last time step of each update. This ensures that all collisions have been applied right before the next frame is rendered. As example, the mesh colliders will update on the following steps if the interval is `2` and the update is advancing `8` time steps.

```None
Step 1: Mesh colliders update.
Step 2:
Step 3:
Step 4: Mesh colliders update.
Step 5:
Step 6:
Step 7: Mesh colliders update.
Step 8: Mesh colliders update (guaranteed on last step).
```

Must be non-negative; negative values are clamped to zero. If zero, the mesh colliders will update every time step.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/meshcollidersupdateinterval)*