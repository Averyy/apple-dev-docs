# fitted(to:eventHandler:)

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
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label> where Input : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>
```

#### Return Value

The fitted fully-connected network multi-label classifier model.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the maximum number of iterations is reached.

> **Note**: This method does not do early-stopping, using a high value for `maximumIterations` may lead to over-fitting. Consider providing a validation set.

This method does not do early-stopping, using a high value for `maximumIterations` may lead to over-fitting. Consider providing a validation set.

## Parameters

- `input`: A sequence of examples used for fitting the classifier.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a fully-connected network multi-label classifier model to a sequence of examples.
- [FullyConnectedNetworkMultiLabelClassifier.Annotation](fullyconnectednetworkmultilabelclassifier/annotation.md)
  The annotation type.
- [FullyConnectedNetworkMultiLabelClassifier.Transformer](fullyconnectednetworkmultilabelclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/fitted(to:eventhandler:))*