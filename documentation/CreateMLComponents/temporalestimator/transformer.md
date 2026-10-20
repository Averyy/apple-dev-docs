# Transformer

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The transformer type created by this estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
associatedtype Transformer : TemporalTransformer
```

## See Also

### Adapting and fitting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](./adaptedassupervised%28annotationtype%29.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](./fitted%28to%29.md)
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/transformer)*