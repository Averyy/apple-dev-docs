# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Encodes a fitted transformer.

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
func encode(_ transformer: Self.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtabularestimator/appending(_:)-1x6qv.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](supervisedtabularestimator/appending(_:)-54zun.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtabularestimator/appending(_:)-r8hb.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/encode(_:to:))*