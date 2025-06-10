# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for the `hasSuffix` operator between a `String?` property and user-supplied values.

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
init(mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType == String, PropertyType.UnwrappedType == String
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.

## See Also

- [init(mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(mappingtransform:)-4dp26.md)
  Declares support for the `hasSuffix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(withresolvers:mappingtransform:)-5rtmw.md)
  Declares support for the `hasSuffix` operator between a `String?` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](hassuffixcomparator/init(withresolvers:mappingtransform:)-7tdan.md)
  Declares support for the `hasSuffix` operator between a `String` property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hassuffixcomparator/init(mappingtransform:)-5cmgi)*