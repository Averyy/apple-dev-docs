# AnchoringComponent.PhysicsSimulation

**Framework**: RealityKit  
**Kind**: enum

Describes the physics simulation space of the entity and its descendants.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum PhysicsSimulation
```

#### Overview

This allows developers to fine-tune which entities with an `AnchoringComponent` interact with each other physically, as opposed to not interacting at all.

## Topics

### Operators
- [static func == (AnchoringComponent.PhysicsSimulation, AnchoringComponent.PhysicsSimulation) -> Bool](anchoringcomponent/physicssimulation-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [AnchoringComponent.PhysicsSimulation.isolated](anchoringcomponent/physicssimulation-swift.enum/isolated.md)
  Simulates the entity and its descendants in the entity’s own physics space.
- [AnchoringComponent.PhysicsSimulation.none](anchoringcomponent/physicssimulation-swift.enum/none.md)
  Opts out the entity and its descendants from having their own physics space.
### Instance Properties
- [var hashValue: Int](anchoringcomponent/physicssimulation-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anchoringcomponent/physicssimulation-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/physicssimulation-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/physicssimulation-swift.enum)*