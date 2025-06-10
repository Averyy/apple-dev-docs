# entities(matching:updatingSystemWhen:)

**Framework**: RealityKit  
**Kind**: method

Returns all entities which pass the query predicate of the query.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
func entities(matching query: EntityQuery, updatingSystemWhen condition: SystemUpdateCondition) -> QueryResult<Entity>
```

## Mentions

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)

#### Discussion

Calling this function can increase the rate at which RealityKit calls the [`update(context:)`](system/update(context:).md) method. If `condition` is not met for the current update, this method returns an empty result.

## Parameters

- `query`: The query identifying which entities you want to fetch.
- `condition`: How often the   is updated (if the query is not empty).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneupdatecontext/entities(matching:updatingsystemwhen:))*