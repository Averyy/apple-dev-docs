# ManipulationComponent.HitTarget

**Framework**: RealityKit  
**Kind**: struct

A component that redirects input to a different entity with a `ManipulationComponent`.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct HitTarget
```

#### Overview

Add this component to an entity and set `redirectedEntity` to another entity that should activate when interaction occurs on the entity with the `HitTarget` component:

```swift
// Configure an entity for interaction.
entityToMove.components.set(ManipulationComponent())

// Create a component redirecting input to `entityToMove`.
let targetComponent = ManipulationComponent.HitTarget(redirectedEntity: entityToMove)

// Apply it to another entity. Now when input occurs on `proxyTarget`,
// the interaction on `entityToMove` will trigger.
proxyTarget.components.set(targetComponent)
```

## Topics

### Initializers
- [init(redirectedEntity: Entity?)](manipulationcomponent/hittarget/init(redirectedentity:).md)
  Initialize a `HitTarget` component redirecting to an entity that has a `ManipulationComponent`.
### Instance Properties
- [var redirectedEntity: Entity?](manipulationcomponent/hittarget/redirectedentity.md)
  The entity to redirect the interaction to.

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/hittarget)*