# EntityQuerySortingOptions

**Framework**: App Intents  
**Kind**: struct

The potential properties you can use to sort the results of a query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct EntityQuerySortingOptions<Entity> where Entity : AppEntity
```

## Topics

### Creating the sorting options
- [init(content: () -> [EntityQuerySortableByProperty<Entity>])](entityquerysortingoptions/init(content:).md)
- [enum EntityQuerySortingOptionsBuilder](entityquerysortingoptionsbuilder.md)
  A result builder that allows you to declaratively describe the sorting options for an entity query.
### Getting the sorting options
- [subscript(Int) -> EntityQuerySortableByProperty<Entity>](entityquerysortingoptions/subscript(_:).md)
### Initializers
- [init()](entityquerysortingoptions/init.md)

## See Also

- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [struct EntityQueryProperties](entityqueryproperties.md)
  A type that provides the properties to include in a property-matched query.
- [class EntityQueryProperty](entityqueryproperty.md)
  An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](entityquerysort.md)
  The properties to use to sort the results when the query runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysortingoptions)*