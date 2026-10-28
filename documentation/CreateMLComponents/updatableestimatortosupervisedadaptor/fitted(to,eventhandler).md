# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a transformer to a sequence of examples, ignoring the annotations and the validation.

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
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer where Input : Sequence, Input.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>
```

## Return Value

The pre-defined transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

### Fitting and Updating
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> Estimator.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Estimator.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, Validation>(inout Estimator.Transformer, with: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws](./update%28_,with,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortosupervisedadaptor/fitted(to:eventhandler:))*