# ClothSimulationEvents.AfterUpdate

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth simulation publishes immediately after performing an update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AfterUpdate
```

## Topics

### Accessing update information
- [let simulationEntity: Entity](clothsimulationevents/afterupdate/simulationentity.md)
  The entity that has the simulation component that this event originates from.
- [let updateCount: UInt64](clothsimulationevents/afterupdate/updatecount.md)
  The total number of updates in the simulation including the update that immediately precedes this event.
### Instance Properties
- [let deltaTime: TimeInterval](clothsimulationevents/afterupdate/deltatime.md)
  The duration of the simulation update, in seconds, that this event represents.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [ClothSimulationEvents.Start](clothsimulationevents/start.md)
  An event type that a cloth simulation publishes immediately after it starts.
- [ClothSimulationEvents.BeforeUpdate](clothsimulationevents/beforeupdate.md)
  An event type that a cloth simulation publishes immediately before performing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationevents/afterupdate)*