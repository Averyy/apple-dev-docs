# EntityQueryProperties

**Framework**: App Intents  
**Kind**: struct

A type that provides the properties to include in a property-matched query.

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
struct EntityQueryProperties<Entity, ComparatorMappingType> where Entity : AppEntity
```

#### Overview

Contains all the supported properties a user can query against an entity for a given query. Declare query properties with a block containing all applicable [`EntityQueryProperty`](entityqueryproperty.md) objects.

#### Example

```swift
var properties = QueryProperties {
    Property(\.$myDate) {
        LessThanComparator { /* ... body of mapping transform ... */ }
        GreaterThanComparator { /* ... body of mapping transform ... */ }
    }
    Property(\.$myArray) {
        ContainsComparator { /* ... body of mapping transform ... */ }
    }
}
```

## Topics

### Creating the query properties
- [init(properties: () -> [EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>])](entityqueryproperties/init(properties:).md)
- [enum EntityQueryPropertiesBuilder](entityquerypropertiesbuilder.md)
  A result builder that allows you to declaratively describe the properties to include in a property-matched query.
### Getting the query properties
- [subscript(Int) -> EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>](entityqueryproperties/subscript(_:).md)

## See Also

- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [class EntityQueryProperty](entityqueryproperty.md)
  An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
- [struct EntityQuerySortingOptions](entityquerysortingoptions.md)
  The potential properties you can use to sort the results of a query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](entityquerysort.md)
  The properties to use to sort the results when the query runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityqueryproperties)*