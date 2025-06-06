# PhysicsSimulationEvents.WillSimulate

**Framework**: RealityKit  
**Kind**: struct

The event raised before the simulation advances to the current frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct WillSimulate
```

## Topics

### Instance Properties
- [let deltaTime: TimeInterval](physicssimulationevents/willsimulate/deltatime.md)
  The time between the last fixed update event and this one.
- [let simulationEntity: Entity](physicssimulationevents/willsimulate/simulationentity.md)
  The root simulation entity associated with the simulation that raised the event.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationevents/willsimulate)*