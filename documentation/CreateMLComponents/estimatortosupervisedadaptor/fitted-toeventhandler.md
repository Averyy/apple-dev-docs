# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of examples, ignoring the annotations and the validation.

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
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer where Input : Sequence, Input.Element == AnnotatedFeature<Estimator.Transformer.Input, Annotation>
```

#### Return Value

The pre-defined transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor/fitted(to:eventhandler:))*