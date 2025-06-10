# init(withResolvers:mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for the `contains` operator between a `String?` property and user-supplied values.

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
init<Spec>(@ResolverSpecificationBuilder<String> withResolvers resolvers: @escaping () -> Spec, mappingTransform: @escaping (InputType) -> ComparatorMappingType) where PropertyType : ExpressibleByNilLiteral, InputType == String, Spec : ResolverSpecification, PropertyType.UnwrappedType == String
```

## Parameters

- `resolvers`: Set of  s to apply when converting user input to the target   type.
- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/containscomparator/init(withresolvers:mappingtransform:)-5j3ie)*