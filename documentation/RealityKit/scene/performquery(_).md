# performQuery(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns all entities of the scene which pass the query.

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
@preconcurrency func performQuery(_ query: EntityQuery) -> QueryResult<Entity>
```

#### Discussion

When in [`update(context:)`](../system/update%28context%29.md), call [`entities(matching:updatingSystemWhen:)`](../sceneupdatecontext/entities%28matching,updatingsystemwhen%29.md) instead of `performQuery`. This allows the [`System`](../system.md) to sleep on some platforms when there is no matching component, reducing unnecessary work.

## See Also

### Finding entities
- [func findEntity(named: String) -> Entity?](./findentity%28named%29.md)
  Searches the scene’s anchor entity hierarchies for an entity with the given name.
- [func findEntity(id: Entity.ID) -> Entity?](./findentity%28id%29.md)
  Returns `Entity` with the given `Entity.ID` in the `Scene`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/performquery(_:))*