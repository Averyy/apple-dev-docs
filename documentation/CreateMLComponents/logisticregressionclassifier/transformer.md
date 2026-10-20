# LogisticRegressionClassifier.Transformer

**Framework**: Create ML Components  
**Kind**: typealias  
**Role**: Type Alias

The transformer type created by this estimator.

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
typealias Transformer = LogisticRegressionClassifierModel<Scalar, Label>
```

## See Also

### Fitting
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a logistic regression classifier model to a sequence of examples while validating with a validation sequence.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifierModel<Scalar, Label>](./fitted%28to,validateon,eventhandler%29.md)
  Fits a logistic regression classifier model to a sequence of examples.
- [LogisticRegressionClassifier.Annotation](./annotation.md)
  The annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/transformer)*