# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for the `contains` operator between an optional `Array` property and user-supplied values.

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
init(mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType : Equatable, InputType == PropertyType.UnwrappedType.Element, PropertyType.UnwrappedType : _SequenceIntentValue, PropertyType.UnwrappedType : Sequence
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.

## See Also

- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-xvws.md)
  Declares support for the `contains` operator between a `AttributedString` property and user-supplied values.
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(mappingtransform:)-3xuvt.md)
  Declares support for the `contains` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](containscomparator/init(withresolvers:mappingtransform:)-4482k.md)
  Declares support for the `contains` operator between an `Array` property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator/init(mappingtransform:)-7rx55)*