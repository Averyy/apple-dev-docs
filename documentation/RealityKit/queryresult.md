# QueryResult

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that returns the results of an entity query.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct QueryResult<Element>
```

#### Overview

You can’t create query result objects. Instead, call [`performQuery(_:)`](./scene/performquery%28_%29.md), which returns a [`QueryResult`](./queryresult.md) containing the entities that meet your specified query criteria.

```swift
// Ask the scene to perform the query and iterate over the returned entities.
scene.performQuery(query).forEach { entity in
    print("Returned entity: \(entity)")
}
```

## Topics

### Creating an iterator
- [QueryResult.Iterator](./queryresult/iterator.md)
  The type of iterator used for entity query results.
- [func makeIterator() -> QueryResult<Element>.Iterator](./queryresult/makeiterator%28%29.md)
  Returns an iterator for the contained entities.
### Default Implementations
- [Sequence Implementations](./queryresult/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Entity queries
- [struct EntityQuery](./entityquery.md)
  An object that retrieves entities from a scene.
- [struct QueryPredicate](./querypredicate.md)
  An object that defines the criteria for an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult)*