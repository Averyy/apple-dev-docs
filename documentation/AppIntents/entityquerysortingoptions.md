# EntityQuerySortingOptions

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

The potential properties you can use to sort the results of a query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct EntityQuerySortingOptions<Entity> where Entity : AppEntity
```

## Topics

### Creating the sorting options
- [init(content: () -> [EntityQuerySortableByProperty<Entity>])](./entityquerysortingoptions/init%28content%29.md)
- [enum EntityQuerySortingOptionsBuilder](./entityquerysortingoptionsbuilder.md)
  A result builder that allows you to declaratively describe the sorting options for an entity query.
### Getting the sorting options
- [subscript(Int) -> EntityQuerySortableByProperty<Entity>](./entityquerysortingoptions/subscript%28_%29.md)
### Initializers
- [init()](./entityquerysortingoptions/init%28%29.md)

## See Also

### Sort options
- [struct EntityQuerySortableByProperty](./entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](./entityquerysort.md)
  The properties to use to sort the results when the query runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysortingoptions)*