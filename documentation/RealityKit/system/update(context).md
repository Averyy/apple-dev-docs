# update(context:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates entities up to once every scene update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency mutating func update(context: SceneUpdateContext)
```

## Mentions

- [Implementing systems for entities in a scene](../implementing-systems-for-entities-in-a-scene.md)

## Discussion

RealityKit calls this method on all registered systems, as often as the `updatingSystemWhen` parameter of [`entities(matching:updatingSystemWhen:)`](../sceneupdatecontext/entities%28matching,updatingsystemwhen%29.md) defines.

The `context` parameter contains a reference to the scene that the [`System`](../system.md) is updating, along with the elapsed time since RealityKit last called the update method for the same scene. Use [`entities(matching:updatingSystemWhen:)`](../sceneupdatecontext/entities%28matching,updatingsystemwhen%29.md) inside this method for the most optimized way to find the matching entities for this [`System`](../system.md).

## Parameters

- `context`: The scene context for the scene to update.

## Default Implementations

### System Implementations
- [func update(context: SceneUpdateContext)](./update%28context%29-3d0qz.md)
  A default implementation that does nothing.

## See Also

### Implementing system logic
- [struct SceneUpdateContext](../sceneupdatecontext.md)
  An object that contains information about the scene to update.
- [struct EntityQuery](../entityquery.md)
  An object that retrieves entities from a scene.
- [struct QueryPredicate](../querypredicate.md)
  An object that defines the criteria for an entity query.
- [struct QueryResult](../queryresult.md)
  An object that returns the results of an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/update(context:))*