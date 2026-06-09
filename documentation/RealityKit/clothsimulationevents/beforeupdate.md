# ClothSimulationEvents.BeforeUpdate

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth simulation publishes immediately before performing an update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BeforeUpdate
```

## Topics

### Inspecting the update
- [let simulationEntity: Entity](clothsimulationevents/beforeupdate/simulationentity.md)
  The entity that has the simulation component that this event originates from.
- [let updateCount: UInt64](clothsimulationevents/beforeupdate/updatecount.md)
  The total number of updates in the simulation including the next update that immediately follows this event.
### Instance Properties
- [let deltaTime: TimeInterval](clothsimulationevents/beforeupdate/deltatime.md)
  The duration of the simulation update, in seconds, that this event represents.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ClothSimulationEvents.Start](clothsimulationevents/start.md)
  An event type that a cloth simulation publishes immediately after it starts.
- [ClothSimulationEvents.AfterUpdate](clothsimulationevents/afterupdate.md)
  An event type that a cloth simulation publishes immediately after performing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationevents/beforeupdate)*