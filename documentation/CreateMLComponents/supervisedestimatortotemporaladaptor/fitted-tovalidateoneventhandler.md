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
func fitted<InputSequence, Validation, FeatureSequence>(to input: InputSequence, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer where InputSequence : Sequence, Validation : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Base.Annotation>, Validation.Element == AnnotatedFeature<FeatureSequence, Base.Annotation>, FeatureSequence.Feature == Base.Transformer.Input
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](supervisedestimatortotemporaladaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [SupervisedEstimatorToTemporalAdaptor.Annotation](supervisedestimatortotemporaladaptor/annotation.md)
  The annotation type.
- [SupervisedEstimatorToTemporalAdaptor.Input](supervisedestimatortotemporaladaptor/input.md)
  The input type.
- [SupervisedEstimatorToTemporalAdaptor.Output](supervisedestimatortotemporaladaptor/output.md)
  The output type.
- [SupervisedEstimatorToTemporalAdaptor.Transformer](supervisedestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/fitted(to:validateon:eventhandler:))*