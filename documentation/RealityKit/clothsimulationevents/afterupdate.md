# ClothSimulationEvents.AfterUpdate

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An event type that a cloth simulation publishes immediately after performing an update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct AfterUpdate
```

## Topics

### Accessing update information
- [let simulationEntity: Entity](./afterupdate/simulationentity.md)
  The entity that has the simulation component that this event originates from.
- [let updateCount: UInt64](./afterupdate/updatecount.md)
  The total number of updates in the simulation including the update that immediately precedes this event.
### Instance Properties
- [let deltaTime: TimeInterval](./afterupdate/deltatime.md)
  The duration of the simulation update, in seconds, that this event represents.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing simulation events
- [ClothSimulationEvents.Start](./start.md)
  An event type that a cloth simulation publishes immediately after it starts.
- [ClothSimulationEvents.BeforeUpdate](./beforeupdate.md)
  An event type that a cloth simulation publishes immediately before performing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationevents/afterupdate)*