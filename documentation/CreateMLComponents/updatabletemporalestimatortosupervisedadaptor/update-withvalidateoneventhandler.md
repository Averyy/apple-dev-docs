# update(_:with:validateOn:eventHandler:)

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
func update<InputSequence, Validation, FeatureSequence>(_ transformer: inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with input: InputSequence, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Validation : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Annotation>, Validation.Element == AnnotatedFeature<FeatureSequence, Annotation>, FeatureSequence.Feature == Estimator.Transformer.Input
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `validation`: A sequence of examples used for validation.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func makeTransformer() -> Estimator.Transformer](updatabletemporalestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/update(_:with:validateon:eventhandler:))*