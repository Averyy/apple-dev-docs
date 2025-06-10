# HasPrefixComparator

**Framework**: App Intents  
**Kind**: class

An object that determines whether the value of a string property has the specified prefix.

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
final class HasPrefixComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : _IntentValue
```

## Topics

### Creating a comparator
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(mappingtransform:)-4i1bf.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(mappingtransform:)-5kri6.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(withresolvers:mappingtransform:)-2n67a.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(withresolvers:mappingtransform:)-48o75.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](entityquerycomparator.md)

## See Also

- [class HasSuffixComparator](hassuffixcomparator.md)
  An object that determines whether the value of a string property has the specified suffix.
- [enum StringComparisonOperator](stringcomparisonoperator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hasprefixcomparator)*