# SceneUpdateContext

**Framework**: RealityKit  
**Kind**: struct

An object that contains information about the scene to update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct SceneUpdateContext
```

## Mentions

- [Passing Metal command objects around your application](passing-metal-command-objects-around-your-application.md)

#### Overview

RealityKit uses a [`SceneUpdateContext`](sceneupdatecontext.md) to pass information to a [`System`](system.md) about the scene it’s currently updating.

## Topics

### Updating a scene
- [var scene: Scene](sceneupdatecontext/scene.md)
  The updating scene.
- [var deltaTime: TimeInterval](sceneupdatecontext/deltatime.md)
  The number of seconds elapsed since the last update.
### Instance Methods
- [func entities(matching: EntityQuery, updatingSystemWhen: SystemUpdateCondition) -> QueryResult<Entity>](sceneupdatecontext/entities(matching:updatingsystemwhen:).md)
  Returns all entities which pass the query predicate of the query.

## See Also

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)
  Apply behaviors and physical effects to the objects and characters in a RealityKit scene with the Entity Component System (ECS).
- [protocol System](system.md)
  An object that affects multiple entities in every update of a RealityKit scene.
- [struct SystemUpdateCondition](systemupdatecondition.md)
  A condition which causes a system to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneupdatecontext)*