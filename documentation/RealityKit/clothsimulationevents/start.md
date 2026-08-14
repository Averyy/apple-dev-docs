# ClothSimulationEvents.Start

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth simulation publishes immediately after it starts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Start
```

#### Overview

A simulation starts once before entering its update loop, at which point it regularly updates.

## Topics

### Accessing the simulation entity
- [let simulationEntity: Entity](clothsimulationevents/start/simulationentity.md)
  The entity that has the simulation component that this event originates from.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [ClothSimulationEvents.BeforeUpdate](clothsimulationevents/beforeupdate.md)
  An event type that a cloth simulation publishes immediately before performing an update.
- [ClothSimulationEvents.AfterUpdate](clothsimulationevents/afterupdate.md)
  An event type that a cloth simulation publishes immediately after performing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationevents/start)*