# PhysicsSimulationEvents.DidSimulate

**Framework**: RealityKit  
**Kind**: struct

The event raised after the simulation advances to the current frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct DidSimulate
```

## Topics

### Instance Properties
- [let deltaTime: TimeInterval](physicssimulationevents/didsimulate/deltatime.md)
  The time between last fixed update event and this one.
- [let simulationEntity: Entity](physicssimulationevents/didsimulate/simulationentity.md)
  The root simulation entity associated with the simulation that raised the event.
- [let simulationRootEntity: Entity?](physicssimulationevents/didsimulate/simulationrootentity.md)
  The root simulation entity associated with the simulation that raised the event.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationevents/didsimulate)*