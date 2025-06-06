# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this tabular estimator with a supervised tabular estimator.

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
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation> where Other : SupervisedTabularEstimator
```

## See Also

- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](tabularestimator/appending(_:)-2i7ef.md)
  Compose this tabular estimator with another tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](tabularestimator/appending(_:)-4d7fj.md)
  Compose this tabular estimator with a tabular transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/appending(_:)-9kf76)*