# ManipulationComponent.HitTargetComponent

**Framework**: RealityKit  
**Kind**: struct

A component that redirects input to a different entity with a `ManipulationComponent`.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct HitTargetComponent
```

#### Overview

Add this component to an entity and set `redirectedEntityID` to the ID of the entity that should activate when interaction occurs on the entity with the `HitTargetComponent`:

```None
// Configure an entity for interaction.
entityToMove.components.set(ManipulationComponent())

// Create a component redirecting input to `entityToMove`.
let targetComponent = ManipulationComponent.HitTargetComponent(redirectedEntityID: entityToMove.id)

// Apply it to another entity. Now when input occurs on `proxyTarget`,
// the interaction on `entityToMove` will trigger.
proxyTarget.components.set(targetComponent)
```

## Topics

### Initializers
- [init(redirectedEntityID: Entity.ID?)](manipulationcomponent/hittargetcomponent/init(redirectedentityid:).md)
  Initialize a `HitTargetComponent` with an entity ID of an entity that has a `ManipulationComponent`.
### Instance Properties
- [var redirectedEntityID: Entity.ID?](manipulationcomponent/hittargetcomponent/redirectedentityid.md)
  The entity ID to redirect the interaction to.

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/hittargetcomponent)*