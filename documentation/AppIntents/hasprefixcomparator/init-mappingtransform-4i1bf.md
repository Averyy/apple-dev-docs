# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.

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
init(mappingTransform: @escaping (InputType) -> ComparatorMappingType) where Property : EntityProperty<String>, PropertyType == String, InputType == String
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.

## See Also

- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(mappingtransform:)-5kri6.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(withresolvers:mappingtransform:)-2n67a.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hasprefixcomparator/init(withresolvers:mappingtransform:)-48o75.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hasprefixcomparator/init(mappingtransform:)-4i1bf)*