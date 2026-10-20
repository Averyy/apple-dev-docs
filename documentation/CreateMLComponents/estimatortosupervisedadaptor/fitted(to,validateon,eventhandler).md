# fitted(to:validateOn:eventHandler:)

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
- watchOS 11.0+

## Declaration

```swift
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>, Validation.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples, ignoring the annotations and the validation.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor/fitted(to:validateon:eventhandler:))*