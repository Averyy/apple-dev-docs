# featureValue(for:)

**Framework**: Core ML  
**Kind**: method  
**Required**: Yes

Accesses the feature value given the feature’s name.

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
func featureValue(for featureName: String) -> MLFeatureValue?
```

#### Return Value

The value of the feature, or nil if no value exists for that name.

## Parameters

- `featureName`: The name of the feature of the desired value.

## See Also

- [var featureNames: Set<String>](mlfeatureprovider/featurenames.md)
  The set of valid feature names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeatureprovider/featurevalue(for:))*