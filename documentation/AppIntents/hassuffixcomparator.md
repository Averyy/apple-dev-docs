# HasSuffixComparator

**Framework**: App Intents  
**Kind**: class

An object that determines whether the value of a string property has the specified suffix.

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
final class HasSuffixComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : _IntentValue
```

## Topics

### Creating a comparator
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(mappingtransform:)-4dp26.md)
  Declares support for the `hasSuffix` operator between a `String` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(mappingtransform:)-5cmgi.md)
  Declares support for the `hasSuffix` operator between a `String?` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(withresolvers:mappingtransform:)-5rtmw.md)
  Declares support for the `hasSuffix` operator between a `String?` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(withresolvers:mappingtransform:)-7tdan.md)
  Declares support for the `hasSuffix` operator between a `String` property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](entityquerycomparator.md)

## See Also

- [class HasPrefixComparator](hasprefixcomparator.md)
  An object that determines whether the value of a string property has the specified prefix.
- [enum StringComparisonOperator](stringcomparisonoperator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hassuffixcomparator)*