# ContainsComparator

**Framework**: App Intents  
**Kind**: class  
**Role**: Class

An object that determines whether the value of sequence property contains the specified value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
final class ContainsComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : _IntentValue
```

## Topics

### Creating a comparator
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-xvws.md)
  Declares support for the `contains` operator between a `AttributedString` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-3xuvt.md)
  Declares support for the `contains` operator between a `String` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-7rx55.md)
  Declares support for the `contains` operator between an optional `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-4482k.md)
  Declares support for the `contains` operator between an `Array` property and user-supplied values.
### Initializers
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-7ya5.md)
  Declares support for the `contains` operator between a `AttributedString?` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-9fn0e.md)
  Declares support for the `contains` operator between a `String?` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28mappingtransform%29-coon.md)
  Declares support for the `contains` operator between an `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-3esov.md)
  Declares support for the `contains` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-5j3ie.md)
  Declares support for the `contains` operator between a `String?` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-7vx0d.md)
  Declares support for the `contains` operator between an optional `Array` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-83nih.md)
  Declares support for the `contains` operator between a `AttributedString` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./containscomparator/init%28withresolvers,mappingtransform%29-wpei.md)
  Declares support for the `contains` operator between a `AttributedString?` property and user-supplied values.

## Relationships

### Inherits From
- [EntityQueryComparator](./entityquerycomparator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator)*