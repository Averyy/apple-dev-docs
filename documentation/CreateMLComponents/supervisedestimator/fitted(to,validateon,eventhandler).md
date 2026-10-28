# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fits a transformer to a sequence of examples while validating with a validation sequence.

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>, Validation.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```

## Mentions

- [Creating a multi-label image classifier](../creating-a-multi-label-image-classifier.md)

## Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## Default Implementations

### SupervisedEstimator Implementations
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,validateon,eventhandler%29-5v8ky.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.

## See Also

### Adapting and fitting
- [func adaptedAsTemporal() -> SupervisedEstimatorToTemporalAdaptor<Self>](./adaptedastemporal%28%29.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](./fitted%28to%29.md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](./fitted%28to,validateon%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/fitted(to:validateon:eventhandler:))*