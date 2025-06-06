# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this supervised tabular estimator with a tabular transformer.

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
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation> where Other : TabularTransformer
```

## See Also

- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtabularestimator/appending(_:)-1x6qv.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtabularestimator/appending(_:)-r8hb.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](supervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/appending(_:)-54zun)*