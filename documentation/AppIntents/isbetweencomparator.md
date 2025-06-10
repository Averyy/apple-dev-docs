# IsBetweenComparator

**Framework**: App Intents  
**Kind**: class

This comparator is only supported for `Date` types in Shortcuts.

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
final class IsBetweenComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : Comparable, InputType == PropertyType.UnwrappedType
```

## Topics

### Initializers
- [init(mappingTransform: (InputType, InputType) -> ComparatorMappingType)](isbetweencomparator/init(mappingtransform:).md)
  Declares support for `Between` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType, InputType) -> ComparatorMappingType)](isbetweencomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Between` comparisons between a property and user-supplied values.

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
- [class GreaterThanOrEqualToComparator](greaterthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is greater than or equal to the specified value.
- [class LessThanComparator](lessthancomparator.md)
  An object that determines whether the value of a comparable property is less than the specified value.
- [class LessThanOrEqualToComparator](lessthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is less than or equal to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/isbetweencomparator)*