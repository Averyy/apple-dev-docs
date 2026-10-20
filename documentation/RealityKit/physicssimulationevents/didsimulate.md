# PhysicsSimulationEvents.DidSimulate

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [let deltaTime: TimeInterval](./didsimulate/deltatime.md)
  The time between last fixed update event and this one.
- [let simulationEntity: Entity](./didsimulate/simulationentity.md)
  The root simulation entity associated with the simulation that raised the event.
- [let simulationRootEntity: Entity?](./didsimulate/simulationrootentity.md)
  The root simulation entity associated with the simulation that raised the event.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationevents/didsimulate)*