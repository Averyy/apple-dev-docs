# EntityQuerySort

**Framework**: App Intents  
**Kind**: struct

The properties to use to sort the results when the query runs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct EntityQuerySort<Entity> where Entity : AppEntity
```

## Topics

### Getting the property details
- [let by: PartialKeyPath<Entity>](entityquerysort/by.md)
### Getting the sort order
- [let order: EntityQuerySort<Entity>.Ordering](entityquerysort/order.md)
- [EntityQuerySort.Ordering](entityquerysort/ordering.md)

## See Also

- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [struct EntityQueryProperties](entityqueryproperties.md)
  A type that provides the properties to include in a property-matched query.
- [class EntityQueryProperty](entityqueryproperty.md)
  An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
- [struct EntityQuerySortingOptions](entityquerysortingoptions.md)
  The potential properties you can use to sort the results of a query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysort)*