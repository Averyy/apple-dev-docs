# performQuery(_:)

**Framework**: RealityKit  
**Kind**: method

Returns all entities of the scene which pass the query.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func performQuery(_ query: EntityQuery) -> QueryResult<Entity>
```

#### Discussion

When in [`update(context:)`](system/update(context:).md), call [`entities(matching:updatingSystemWhen:)`](sceneupdatecontext/entities(matching:updatingsystemwhen:).md) instead of `performQuery`. This allows the [`System`](system.md) to sleep on some platforms when there is no matching component, reducing unnecessary work.

## See Also

- [func findEntity(named: String) -> Entity?](scene/findentity(named:).md)
  Searches the scene’s anchor entity hierarchies for an entity with the given name.
- [func findEntity(id: Entity.ID) -> Entity?](scene/findentity(id:).md)
  Returns `Entity` with the given `Entity.ID` in the `Scene`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/performquery(_:))*