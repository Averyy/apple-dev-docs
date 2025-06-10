# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init

Declares support for `Comparable` `>` comparisons between a property and user-supplied values.

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
init(mappingTransform: @escaping (PropertyType.UnwrappedType) -> ComparatorMappingType)
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the   output type.

## See Also

- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](greaterthanorequaltocomparator/init(withresolvers:mappingtransform:).md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/greaterthanorequaltocomparator/init(mappingtransform:))*