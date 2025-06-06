# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a fully-connected network multi-label classifier model to a sequence of examples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label> where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>, Validation.Element == AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>
```

#### Return Value

The fitted fully-connected network multi-label classifier model.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the validation loss stops improving or when the maximum number of iterations is reached.

## Parameters

- `input`: A sequence of examples used for fitting the classifier.
- `validation`: A sequence of examples used for validating the fitted multi-label classifier.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/fitted(to:eventhandler:).md)
  Fits a fully-connected network multi-label classifier model to a sequence of examples.
- [FullyConnectedNetworkMultiLabelClassifier.Annotation](fullyconnectednetworkmultilabelclassifier/annotation.md)
  The annotation type.
- [FullyConnectedNetworkMultiLabelClassifier.Transformer](fullyconnectednetworkmultilabelclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/fitted(to:validateon:eventhandler:))*