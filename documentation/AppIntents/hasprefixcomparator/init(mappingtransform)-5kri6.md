# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.

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
init(mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType == String, PropertyType.UnwrappedType == String
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the `ComparatorMappingType` output type.

## See Also

### Creating a comparator
- [init(mappingTransform: (InputType) -> ComparatorMappingType)](./init%28mappingtransform%29-4i1bf.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./init%28withresolvers,mappingtransform%29-2n67a.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (InputType) -> ComparatorMappingType)](./init%28withresolvers,mappingtransform%29-48o75.md)
  Declares support for the `hasPrefix` operator between a `String` property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hasprefixcomparator/init(mappingtransform:)-5kri6)*