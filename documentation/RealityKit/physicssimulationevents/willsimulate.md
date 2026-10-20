# PhysicsSimulationEvents.WillSimulate

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event raised before the simulation advances to the current frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct WillSimulate
```

## Topics

### Instance Properties
- [let deltaTime: TimeInterval](./willsimulate/deltatime.md)
  The time between the last fixed update event and this one.
- [let simulationEntity: Entity](./willsimulate/simulationentity.md)
  The root simulation entity associated with the simulation that raised the event.
- [let simulationRootEntity: Entity?](./willsimulate/simulationrootentity.md)
  The root simulation entity associated with the simulation that raised the event.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationevents/willsimulate)*