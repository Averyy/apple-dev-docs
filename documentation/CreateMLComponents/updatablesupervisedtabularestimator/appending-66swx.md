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
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation> where Other : TabularTransformer, Self.Annotation : Equatable
```

## See Also

- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtabularestimator/appending(_:)-2cr8d.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtabularestimator/appending(_:)-5wg05.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtabularestimator/appending(_:)-66swx)*