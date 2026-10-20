# adaptedAsSupervised(annotationType:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exposes this temporal estimator as a supervised temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type = Annotation.self) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation> where Annotation : Equatable, Annotation : Sendable
```

## See Also

### Adapting and fitting
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](./fitted%28to%29.md)
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [associatedtype Transformer : TemporalTransformer](./transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/adaptedassupervised(annotationtype:))*