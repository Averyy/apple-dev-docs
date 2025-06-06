# isAllowedValue(_:)

**Framework**: Core ML  
**Kind**: method

Checks whether the model will accept an input feature value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func isAllowedValue(_ value: MLFeatureValue) -> Bool
```

#### Return Value

`True` if the given `MLFeatureValue` is acceptable to the model’s input feature, `false` otherwise.

## Parameters

- `value`: Given the  , is it compatible with the   of this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturedescription/isallowedvalue(_:))*