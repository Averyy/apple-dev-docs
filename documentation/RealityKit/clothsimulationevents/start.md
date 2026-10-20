# ClothSimulationEvents.Start

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An event type that a cloth simulation publishes immediately after it starts.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Start
```

#### Overview

A simulation starts once before entering its update loop, at which point it regularly updates.

## Topics

### Accessing the simulation entity
- [let simulationEntity: Entity](./start/simulationentity.md)
  The entity that has the simulation component that this event originates from.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing simulation events
- [ClothSimulationEvents.BeforeUpdate](./beforeupdate.md)
  An event type that a cloth simulation publishes immediately before performing an update.
- [ClothSimulationEvents.AfterUpdate](./afterupdate.md)
  An event type that a cloth simulation publishes immediately after performing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationevents/start)*