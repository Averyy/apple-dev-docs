# init(withResolvers:mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for `Between` comparisons between a property and user-supplied values.

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
init<Spec>(@ResolverSpecificationBuilder<InputType> withResolvers resolvers: @escaping () -> Spec, mappingTransform: @escaping (InputType, InputType) -> ComparatorMappingType) where Spec : ResolverSpecification
```

## Parameters

- `resolvers`: Set of  s to apply when converting user input to the target   type.
- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/isbetweencomparator/init(withresolvers:mappingtransform:))*