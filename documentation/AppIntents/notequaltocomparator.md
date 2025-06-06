# NotEqualToComparator

**Framework**: App Intents  
**Kind**: class

An object that determines whether the value of an equatable property is not equal to the specified value.

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
final class NotEqualToComparator<Property, PropertyType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Equatable, PropertyType : Sendable
```

## Topics

### Creating a comparator
- [init(mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.
- [init(mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](entityquerycomparator.md)

## See Also

- [class EqualToComparator](equaltocomparator.md)
  An object that determines whether the value of an equatable property is equal to the specified value.
- [class GreaterThanComparator](greaterthancomparator.md)
  An object that determines whether the value of a comparable property is greater than the specified value.
- [class GreaterThanOrEqualToComparator](greaterthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is greater than or equal to the specified value.
- [class LessThanComparator](lessthancomparator.md)
  An object that determines whether the value of a comparable property is less than the specified value.
- [class LessThanOrEqualToComparator](lessthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is less than or equal to the specified value.
- [class IsBetweenComparator](isbetweencomparator.md)
  This comparator is only supported for `Date` types in Shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/notequaltocomparator)*