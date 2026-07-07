# ClothBodyEvents.NewSimulationPositions

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth body publishes (before simulation update) when its new positions are available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NewSimulationPositions
```

#### Overview

This event should be treated as having a non-escapable lifetime. Some of its data is no longer available after its lifetime has ended.

## Topics

### Accessing local space positions
- [var localSpacePositions: Span<SIMD3<Float>>](clothbodyevents/newsimulationpositions/localspacepositions.md)
  The new simulation positions of the body’s particles, in local space.
- [func withLocalSpacePositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothbodyevents/newsimulationpositions/withlocalspacepositions(_:).md)
  Provides access to the new simulation positions of the body’s particles, in local space.
### Accessing simulation space positions
- [var simulationSpacePositions: Span<SIMD3<Float>>](clothbodyevents/newsimulationpositions/simulationspacepositions.md)
  The new simulation positions of the body’s particles, in simulation space.
- [func withSimulationSpacePositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothbodyevents/newsimulationpositions/withsimulationspacepositions(_:).md)
  Provides access to the new simulation positions of the body’s particles, in simulation space.
### Identifying the event source
- [let bodyEntity: Entity](clothbodyevents/newsimulationpositions/bodyentity.md)
  The entity that has the body component that this event originates from.
- [let updateCount: UInt64](clothbodyevents/newsimulationpositions/updatecount.md)
  The simulation update that this event originates from.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodyevents/newsimulationpositions)*