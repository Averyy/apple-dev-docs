# findEntity(named:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Searches the scene’s anchor entity hierarchies for an entity with the given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func findEntity(named name: String) -> Entity?
```

## Return Value

The first entity found with the given name, or `nil` if none is found.

## Discussion

The [`findEntity(named:)`](./findentity%28named%29.md) method conducts a depth-first, recursive search over all of the scene’s entities for one whose [`name`](../entity/name.md) property matches the given name. The method returns the first match. Entity names need not be unique.

## Parameters

- `name`: The name of the entity for which to search.

## See Also

### Finding entities
- [func performQuery(EntityQuery) -> QueryResult<Entity>](./performquery%28_%29.md)
  Returns all entities of the scene which pass the query.
- [func findEntity(id: Entity.ID) -> Entity?](./findentity%28id%29.md)
  Returns `Entity` with the given `Entity.ID` in the `Scene`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/findentity(named:))*