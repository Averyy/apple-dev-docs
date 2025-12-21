# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<InputSequence, FeatureSequence>(to input: InputSequence, eventHandler: EventHandler? = nil) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer where InputSequence : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Annotation>, FeatureSequence.Feature == Estimator.Transformer.Input
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](temporalestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor/fitted(to:eventhandler:))*