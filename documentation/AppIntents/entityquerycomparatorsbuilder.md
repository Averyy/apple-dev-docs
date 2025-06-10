# EntityQueryComparatorsBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe the comparators for a queryable property.

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
@resultBuilder
enum EntityQueryComparatorsBuilder<Entity, Subject, Property, PropertyType, ComparatorMappingType> where Entity : AppEntity, Subject : AppEntity, Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable
```

## Topics

### Building query comparators
- [static func buildBlock(AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>...) -> [AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>]](entityquerycomparatorsbuilder/buildblock(_:).md)
- [struct AnyEntityQueryComparator](anyentityquerycomparator.md)
  A type that erases the type information of the underlying query comparator.
- [static func buildExpression(EntityQueryComparator<Property, PropertyType, PropertyType.UnwrappedType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-4g6f9.md)
- [static func buildExpression(EntityQueryComparator<Property, PropertyType, PropertyType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-5tlbq.md)
- [static func buildExpression<InputType>(ContainsComparator<Property, PropertyType, InputType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-6v6cj.md)
- [static func buildExpression<InputType>(IsBetweenComparator<Property, PropertyType, InputType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-8jx4k.md)
- [class EntityQueryComparator](entityquerycomparator.md)
  The base class for all concrete entity query comparators.

## See Also

- [convenience init(KeyPath<Subject, Property>, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [init(KeyPath<Subject, Property>, entityProvider: (Entity) -> Subject, comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)](entityqueryproperty/init(_:entityprovider:comparators:).md)
  Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.
- [EntityQueryProperty.QueryComparators](entityqueryproperty/querycomparators.md)
  A type alias for the type that represents a collection of query comparators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparatorsbuilder)*