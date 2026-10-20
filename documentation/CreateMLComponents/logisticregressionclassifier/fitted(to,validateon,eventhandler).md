# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a logistic regression classifier model to a sequence of examples.

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> LogisticRegressionClassifierModel<Scalar, Label> where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>, Validation.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>
```

#### Return Value

The fitted logistic regression classifier model.

## Parameters

- `input`: A sequence of examples used for fitting the classifier.
- `validation`: A sequence of examples used for validating the fitted classifier.
- `eventHandler`: An event handler. This method reports accuracy metrics.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/fitted(to:eventhandler:).md)
  Fits a logistic regression classifier model to a sequence of examples while validating with a validation sequence.
- [LogisticRegressionClassifier.Annotation](logisticregressionclassifier/annotation.md)
  The annotation type.
- [LogisticRegressionClassifier.Transformer](logisticregressionclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/fitted(to:validateon:eventhandler:))*