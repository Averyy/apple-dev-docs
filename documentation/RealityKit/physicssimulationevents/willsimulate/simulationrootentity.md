# simulationRootEntity

**Framework**: RealityKit  
**Kind**: property

The root simulation entity associated with the simulation that raised the event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let simulationRootEntity: Entity?
```

#### Discussion

This entity is `nil` if the physics simulation is the default global one that covers all entities in the hierarchy. Use [`PhysicsSimulationComponent`](physicssimulationcomponent.md) to construct a custom physics simulation for a subtree of entities that you have access to.  The event from this custom simulation reports a non-`nil` root simulation entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationevents/willsimulate/simulationrootentity)*