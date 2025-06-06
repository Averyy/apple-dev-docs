# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a logistic regression classifier model to a sequence of examples while validating with a validation sequence.

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
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer where Input : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifierModel<Scalar, Label>](logisticregressionclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a logistic regression classifier model to a sequence of examples.
- [LogisticRegressionClassifier.Annotation](logisticregressionclassifier/annotation.md)
  The annotation type.
- [LogisticRegressionClassifier.Transformer](logisticregressionclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/fitted(to:eventhandler:))*