# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with a supervised tabular estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation> where Other : SupervisedTabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator/appending(_:)-323zy)*