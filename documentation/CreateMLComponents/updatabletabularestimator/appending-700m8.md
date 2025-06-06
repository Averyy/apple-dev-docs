# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable tabular estimator with another updatable tabular estimator.

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
func appending<Other>(_ other: Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>> where Other : UpdatableTabularEstimator
```

## See Also

- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](updatabletabularestimator/appending(_:)-3sl33.md)
  Composes this updatable tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](updatabletabularestimator/appending(_:)-9shn1.md)
  Composes this updatable tabular estimator with an updatable supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimator/appending(_:)-700m8)*