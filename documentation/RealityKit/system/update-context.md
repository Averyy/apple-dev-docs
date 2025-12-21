# update(context:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Updates entities up to once every scene update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency mutating func update(context: SceneUpdateContext)
```

## Mentions

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)

#### Discussion

RealityKit calls this method on all registered systems, as often as the `updatingSystemWhen` parameter of [`entities(matching:updatingSystemWhen:)`](sceneupdatecontext/entities(matching:updatingsystemwhen:).md) defines.

The `context` parameter contains a reference to the scene that the [`System`](system.md) is updating, along with the elapsed time since RealityKit last called the update method for the same scene. Use [`entities(matching:updatingSystemWhen:)`](sceneupdatecontext/entities(matching:updatingsystemwhen:).md) inside this method for the most optimized way to find the matching entities for this [`System`](system.md).

## Parameters

- `context`: The scene context for the scene to update.

## See Also

- [struct SceneUpdateContext](sceneupdatecontext.md)
  An object that contains information about the scene to update.
- [struct EntityQuery](entityquery.md)
  An object that retrieves entities from a scene.
- [struct QueryPredicate](querypredicate.md)
  An object that defines the criteria for an entity query.
- [struct QueryResult](queryresult.md)
  An object that returns the results of an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/update(context:))*