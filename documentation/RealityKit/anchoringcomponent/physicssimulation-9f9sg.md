# AnchoringComponent.PhysicsSimulation

**Framework**: RealityKit  
**Kind**: enum

Describes the physics simulation space of the entity and its descendants.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
enum PhysicsSimulation
```

#### Overview

This allows developers to fine-tune which entities with an `AnchoringComponent` interact with each other physically, as opposed to not interacting at all.

## Topics

### Enumeration Cases
- [AnchoringComponent.PhysicsSimulation.isolated](anchoringcomponent/physicssimulation-9f9sg/isolated.md)
  Simulates the entity and its descendants in the entity’s own physics space.
- [AnchoringComponent.PhysicsSimulation.none](anchoringcomponent/physicssimulation-9f9sg/none.md)
  Opts out the entity and its descendants from having their own physics space.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/physicssimulation-9f9sg)*