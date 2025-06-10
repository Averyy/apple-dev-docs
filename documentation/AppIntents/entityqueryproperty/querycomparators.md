# EntityQueryProperty.QueryComparators

**Framework**: App Intents  
**Kind**: typealias

A type alias for the type that represents a collection of query comparators.

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
typealias QueryComparators = [AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>]
```

## See Also

- [convenience init(KeyPath<Subject, Property>, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [init(KeyPath<Subject, Property>, entityProvider: (Entity) -> Subject, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:entityprovider:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [enum EntityQueryComparatorsBuilder](entityquerycomparatorsbuilder.md)
  A result builder that allows you to declaratively describe the comparators for a queryable property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityqueryproperty/querycomparators)*