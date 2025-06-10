# ContainsComparator

**Framework**: App Intents  
**Kind**: class

An object that determines whether the value of sequence property contains the specified value.

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
final class ContainsComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : _IntentValue
```

## Topics

### Creating a comparator
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-xvws.md)
  Declares support for the `contains` operator between a `AttributedString` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-3xuvt.md)
  Declares support for the `contains` operator between a `String` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-7rx55.md)
  Declares support for the `contains` operator between an optional `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-4482k.md)
  Declares support for the `contains` operator between an `Array` property and user-supplied values.
### Initializers
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-7ya5.md)
  Declares support for the `contains` operator between a `AttributedString?` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-9fn0e.md)
  Declares support for the `contains` operator between a `String?` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-coon.md)
  Declares support for the `contains` operator between an `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-3esov.md)
  Declares support for the `contains` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-5j3ie.md)
  Declares support for the `contains` operator between a `String?` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-7vx0d.md)
  Declares support for the `contains` operator between an optional `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-83nih.md)
  Declares support for the `contains` operator between a `AttributedString` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-wpei.md)
  Declares support for the `contains` operator between a `AttributedString?` property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](entityquerycomparator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator)*