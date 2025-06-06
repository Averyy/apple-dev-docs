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

## See Also

- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](tabulartransformer/appending(_:)-3ah47.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](tabulartransformer/appending(_:)-3cljt.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](tabulartransformer/appending(_:)-5xcrt.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](tabulartransformer/appending(_:)-6klpi.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](tabulartransformer/appending(_:)-8jrnz.md)
  Compose this tabular transformer with a tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformer/appending(_:)-7sy5c)*