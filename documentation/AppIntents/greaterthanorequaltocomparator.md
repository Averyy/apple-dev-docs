# GreaterThanOrEqualToComparator

**Framework**: App Intents  
**Kind**: class

An object that determines whether the value of a comparable property is greater than or equal to the specified value.

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
final class GreaterThanOrEqualToComparator<Property, PropertyType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, PropertyType.UnwrappedType : Comparable
```

## Topics

### Creating a comparator
- [init(mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.
- [init(mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](entityquerycomparator.md)

## See Also

- [class EqualToComparator](equaltocomparator.md)
  An object that determines whether the value of an equatable property is equal to the specified value.
- [class NotEqualToComparator](notequaltocomparator.md)
  An object that determines whether the value of an equatable property is not equal to the specified value.
- [class GreaterThanComparator](greaterthancomparator.md)
  An object that determines whether the value of a comparable property is greater than the specified value.
- [class LessThanComparator](lessthancomparator.md)
  An object that determines whether the value of a comparable property is less than the specified value.
- [class LessThanOrEqualToComparator](lessthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is less than or equal to the specified value.
- [class IsBetweenComparator](isbetweencomparator.md)
  This comparator is only supported for `Date` types in Shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/greaterthanorequaltocomparator)*