# SupervisedEstimatorToTemporalAdaptor.Transformer

**Framework**: Create ML Components  
**Kind**: typealias  
**Role**: Type Alias

The transformer type created by this estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
typealias Transformer = TransformerToTemporalAdaptor<Base.Transformer>
```

## See Also

### Fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [SupervisedEstimatorToTemporalAdaptor.Annotation](./annotation.md)
  The annotation type.
- [SupervisedEstimatorToTemporalAdaptor.Input](./input.md)
  The input type.
- [SupervisedEstimatorToTemporalAdaptor.Output](./output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/transformer)*