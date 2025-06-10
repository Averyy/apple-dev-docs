# buildExpression(_:)

**Framework**: App Intents  
**Kind**: method

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
static func buildExpression(_ expression: EntityQueryComparator<Property, PropertyType, PropertyType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>
```

## See Also

- [static func buildBlock(AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>...) -> [AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>]](entityquerycomparatorsbuilder/buildblock(_:).md)
- [struct AnyEntityQueryComparator](anyentityquerycomparator.md)
  A type that erases the type information of the underlying query comparator.
- [static func buildExpression(EntityQueryComparator<Property, PropertyType, PropertyType.UnwrappedType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-4g6f9.md)
- [static func buildExpression<InputType>(ContainsComparator<Property, PropertyType, InputType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-6v6cj.md)
- [static func buildExpression<InputType>(IsBetweenComparator<Property, PropertyType, InputType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>](entityquerycomparatorsbuilder/buildexpression(_:)-8jx4k.md)
- [class EntityQueryComparator](entityquerycomparator.md)
  The base class for all concrete entity query comparators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparatorsbuilder/buildexpression(_:)-5tlbq)*