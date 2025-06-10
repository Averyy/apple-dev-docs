# init(withResolvers:mappingTransform:)

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
init<Spec>(@ResolverSpecificationBuilder<AttributedString> withResolvers resolvers: @escaping () -> Spec, mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType == AttributedString, Spec : ResolverSpecification, PropertyType.UnwrappedType == AttributedString
```

## Parameters

- `resolvers`: Set of  s to apply when converting user input to the target   type.
- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator/init(withresolvers:mappingtransform:)-wpei)*