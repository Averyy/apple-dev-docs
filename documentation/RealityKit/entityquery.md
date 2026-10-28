# EntityQuery

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that retrieves entities from a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct EntityQuery
```

## Mentions

- [Implementing systems for entities in a scene](./implementing-systems-for-entities-in-a-scene.md)
- [Implementing scene understanding and reconstruction in your RealityKit app](./realitykit-scene-understanding.md)

## Overview

Use entity queries to iterate through all entities in a RealityKit scene that meet certain criteria. To specify which entities to retrieve, use a [`QueryPredicate`](./querypredicate.md).

To execute the query, pass it into the scene’s [`performQuery(_:)`](./scene/performquery%28_%29.md) method and then iterate over the results.

```swift
// Build a query to retrieve all anchor components.
let query = EntityQuery(where: .has(AnchorComponent.self))

// Find and modify the scene's entities that have an anchor component.
scene.performQuery(query).forEach { entity in
    // Make any needed changes to entities.
}
```

## Topics

### Creating an entity query
- [init()](./entityquery/init%28%29.md)
  Creates a query that returns all entities in a scene.
- [init(where: QueryPredicate<Entity>)](./entityquery/init%28where%29.md)
  Creates a query that returns all entities in a scene that match specific criteria.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Entity queries
- [struct QueryPredicate](./querypredicate.md)
  An object that defines the criteria for an entity query.
- [struct QueryResult](./queryresult.md)
  An object that returns the results of an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityquery)*