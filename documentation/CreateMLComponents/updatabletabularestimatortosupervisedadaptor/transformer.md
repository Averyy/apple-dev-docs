# UpdatableTabularEstimatorToSupervisedAdaptor.Transformer

**Framework**: Create ML Components  
**Kind**: typealias

The transformer type created by this estimator.

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
typealias Transformer = Estimator.Transformer
```

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletabularestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame.
- [func makeTransformer() -> Estimator.Transformer](updatabletabularestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatabletabularestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame containing examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor/transformer)*