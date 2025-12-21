# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of examples while validating with a validation sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<InputSequence, Validation, FeatureSequence>(to input: InputSequence, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer where InputSequence : Sequence, Validation : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Annotation>, Validation.Element == AnnotatedFeature<FeatureSequence, Annotation>, FeatureSequence.Feature == Estimator.Transformer.Input
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> Estimator.Transformer](updatabletemporalestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, Validation, FeatureSequence>(inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:))*