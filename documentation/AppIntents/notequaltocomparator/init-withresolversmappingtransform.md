# init(withResolvers:mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Spec>(@ResolverSpecificationBuilder<PropertyType.UnwrappedType> withResolvers resolvers: @escaping () -> Spec, mappingTransform: @escaping (PropertyType) -> ComparatorMappingType) where Spec : ResolverSpecification
```

## Parameters

- `resolvers`: Set of  s to apply when converting user input to the target   type.
- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.

## See Also

- [init(mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.
- [init(mappingTransform: (PropertyType) -> ComparatorMappingType)](notequaltocomparator/init(mappingtransform:).md)
  Declares support for `Equatable` `!=` comparisons between a property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/notequaltocomparator/init(withresolvers:mappingtransform:))*