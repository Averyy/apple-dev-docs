# init(_:entityProvider:comparators:)

**Framework**: App Intents  
**Kind**: init

Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.

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
init(_ keyPath: KeyPath<Subject, Property>, entityProvider: @escaping (Entity) -> Subject, @EntityQueryComparatorsBuilder<Entity, Subject, Property, PropertyType, ComparatorMappingType> comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)
```

## Parameters

- `keyPath`: The keypath to the property that this EntityQueryProperty applies to. The target   property type determines which comparator modifiers will be available.
- `entityProvider`: Closure which, given a   instance, returns the appropriate    instance to apply  s to.
- `comparators`: The set of   that this property supports being queried by.

## See Also

- [convenience init(KeyPath<Subject, Property>, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [EntityQueryProperty.QueryComparators](entityqueryproperty/querycomparators.md)
  A type alias for the type that represents a collection of query comparators.
- [enum EntityQueryComparatorsBuilder](entityquerycomparatorsbuilder.md)
  A result builder that allows you to declaratively describe the comparators for a queryable property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityqueryproperty/init(_:entityprovider:comparators:))*