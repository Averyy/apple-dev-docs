# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a fully connected network classifier model to a sequence of examples.

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkClassifierModel<Scalar, Label> where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>, Validation.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>
```

#### Return Value

The fitted fully connected network classifier model.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the validation loss stops improving or when the maximum number of iterations is reached.

## Parameters

- `input`: A sequence of examples used for fitting the classifier.
- `validation`: A sequence of examples used for validating the fitted classifier.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/fitted(to:eventhandler:).md)
  Fits a fully connected network classifier model to a sequence of examples.
- [FullyConnectedNetworkClassifier.Annotation](fullyconnectednetworkclassifier/annotation.md)
  The annotation type.
- [FullyConnectedNetworkClassifier.Transformer](fullyconnectednetworkclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/fitted(to:validateon:eventhandler:))*