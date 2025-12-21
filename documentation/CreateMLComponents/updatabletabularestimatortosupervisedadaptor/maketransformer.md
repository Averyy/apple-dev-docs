# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method

Creates a default-initialized transformer suitable for incremental fitting.

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
func makeTransformer() -> Estimator.Transformer
```

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletabularestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame.
- [func update(inout UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatabletabularestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame containing examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor/maketransformer())*