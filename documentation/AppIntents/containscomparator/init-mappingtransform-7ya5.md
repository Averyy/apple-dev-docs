# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for the `contains` operator between a `AttributedString?` property and user-supplied values.

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
init(mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType == AttributedString, PropertyType.UnwrappedType == AttributedString
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator/init(mappingtransform:)-7ya5)*