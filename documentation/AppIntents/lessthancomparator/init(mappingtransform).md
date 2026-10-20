# init(mappingTransform:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Declares support for `Comparable` `>` comparisons between a property and user-supplied values.

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
init(mappingTransform: @escaping (PropertyType.UnwrappedType) -> ComparatorMappingType)
```

## Parameters

- `mappingTransform`: Closure that transforms the user-supplied value into the `ComparatorMappingType` output type.

## See Also

### Creating a comparator
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](./init%28withresolvers,mappingtransform%29.md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.
- [init<Spec>(withResolvers: () -> Spec, mappingTransform: (PropertyType.UnwrappedType) -> ComparatorMappingType)](./init%28withresolvers,mappingtransform%29.md)
  Declares support for `Comparable` `>` comparisons between a property and user-supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/lessthancomparator/init(mappingtransform:))*