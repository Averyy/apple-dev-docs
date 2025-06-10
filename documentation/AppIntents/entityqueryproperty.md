# EntityQueryProperty

**Framework**: App Intents  
**Kind**: class

An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.

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
final class EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType> where Entity : AppEntity, Subject : AppEntity, Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable
```

#### Overview

Entity query properties are defined by by providing a `KeyPath` to an [`AppEntity`](appentity.md) property in your data model that this property applies to and then specify the set of supported [`EntityQueryComparator`](entityquerycomparator.md)s for this property.

`EntityQueryProperty` allows you to define more than one [`EntityQueryComparator`](entityquerycomparator.md) with functionality beyond strict equality. The set of comparators available depends on the underlying property type. For example, an [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable) property type will allow for [`EqualToComparator`](equaltocomparator.md) and [`NotEqualToComparator`](notequaltocomparator.md) comparators while a [`Comparable`](https://developer.apple.com/documentation/Swift/Comparable) property type will add support for [`GreaterThanComparator`](greaterthancomparator.md), [`GreaterThanOrEqualToComparator`](greaterthanorequaltocomparator.md), [`LessThanComparator`](lessthancomparator.md), and [`LessThanOrEqualToComparator`](lessthanorequaltocomparator.md) comparators. See [`Comparator`](https://developer.apple.com/documentation/Foundation/Comparator) for more details on available comparators.

An `EntityQueryProperty` doesn’t necessarily need to apply to a property of its parent Query `Entity`.

Consider the scenario where you have an application containing Photo and Album entities, and you want to support querying photos by the name of their containing album. Within a [`EntityPropertyQuery`](entitypropertyquery.md) in which `Entity` is Photo, you can define a `EntityQueryProperty` mapping to a name property of the Album entity, as long as you supply a closure for `entityProvider` that contains the logic to get from a Photo entity to an Album entity.

See [`init(_:entityProvider:comparators:)`](entityqueryproperty/init(_:entityprovider:comparators:).md) for details.

## Topics

### Creating queryable properties
- [convenience init(KeyPath<Subject, Property>, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [init(KeyPath<Subject, Property>, entityProvider: (Entity) -> Subject, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:entityprovider:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [EntityQueryProperty.QueryComparators](entityqueryproperty/querycomparators.md)
  A type alias for the type that represents a collection of query comparators.
- [enum EntityQueryComparatorsBuilder](entityquerycomparatorsbuilder.md)
  A result builder that allows you to declaratively describe the comparators for a queryable property.

## Relationships

### Inherits From
- [EntityQueryPropertyDeclaration](entityquerypropertydeclaration.md)

## See Also

- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [struct EntityQueryProperties](entityqueryproperties.md)
  A type that provides the properties to include in a property-matched query.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
- [struct EntityQuerySortingOptions](entityquerysortingoptions.md)
  The potential properties you can use to sort the results of a query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](entityquerysort.md)
  The properties to use to sort the results when the query runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityqueryproperty)*