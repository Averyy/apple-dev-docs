# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fits a transformer to a sequence of examples.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func fitted<InputSequence>(to input: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer where InputSequence : Sequence, InputSequence.Element : TemporalSequence, Self.Transformer.Input == InputSequence.Element.Feature
```

## Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

### Adapting and fitting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](./adaptedassupervised%28annotationtype%29.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](./fitted%28to%29.md)
- [associatedtype Transformer : TemporalTransformer](./transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/fitted(to:eventhandler:))*