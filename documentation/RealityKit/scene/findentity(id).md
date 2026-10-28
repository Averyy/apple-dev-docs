# findEntity(id:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns `Entity` with the given `Entity.ID` in the `Scene`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func findEntity(id: Entity.ID) -> Entity?
```

## Return Value

`Entity` with the given `Entity.ID`, or `nil` if no such `Entity` is found in the `Scene`.

## Discussion

> **Note**: This method uses efficient mapping from `Entity.ID` to `Entity`, not linear traversal of all Entities in the `Scene`.

## Parameters

- `id`: `Entity.ID` obtained from `Entity.id`

## See Also

### Finding entities
- [func findEntity(named: String) -> Entity?](./findentity%28named%29.md)
  Searches the scene’s anchor entity hierarchies for an entity with the given name.
- [func performQuery(EntityQuery) -> QueryResult<Entity>](./performquery%28_%29.md)
  Returns all entities of the scene which pass the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/findentity(id:))*