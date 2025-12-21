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
- watchOS 11.0+

## Declaration

```swift
func update<InputSequence, Validation>(_ transformer: inout Estimator.Transformer, with input: InputSequence, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Validation : Sequence, InputSequence.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>, Validation.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `validation`: A sequence of examples used for validation.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples, ignoring the annotations and the validation.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> Estimator.Transformer](updatableestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Estimator.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatableestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortosupervisedadaptor/update(_:with:validateon:eventhandler:))*