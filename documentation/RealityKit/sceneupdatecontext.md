# SceneUpdateContext

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that contains information about the scene to update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct SceneUpdateContext
```

## Mentions

- [Passing Metal command objects around your application](./passing-metal-command-objects-around-your-application.md)

## Overview

RealityKit uses a [`SceneUpdateContext`](./sceneupdatecontext.md) to pass information to a [`System`](./system.md) about the scene it’s currently updating.

## Topics

### Updating a scene
- [var scene: Scene](./sceneupdatecontext/scene.md)
  The updating scene.
- [var deltaTime: TimeInterval](./sceneupdatecontext/deltatime.md)
  The number of seconds elapsed since the last update.
### Instance Methods
- [func entities(matching: EntityQuery, updatingSystemWhen: SystemUpdateCondition) -> QueryResult<Entity>](./sceneupdatecontext/entities%28matching,updatingsystemwhen%29.md)
  Returns all entities which pass the query predicate of the query.

## See Also

### Implementing system logic
- [func update(context: SceneUpdateContext)](./system/update%28context%29.md)
  Updates entities up to once every scene update.
- [struct EntityQuery](./entityquery.md)
  An object that retrieves entities from a scene.
- [struct QueryPredicate](./querypredicate.md)
  An object that defines the criteria for an entity query.
- [struct QueryResult](./queryresult.md)
  An object that returns the results of an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneupdatecontext)*