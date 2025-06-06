# adaptedAsSupervised(annotationType:)

**Framework**: Create ML Components  
**Kind**: method

Exposes this temporal estimator as a supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type = Annotation.self) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation> where Annotation : Equatable, Annotation : Sendable
```

## See Also

- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](temporalestimator/fitted(to:).md)
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](temporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [associatedtype Transformer : TemporalTransformer](temporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/adaptedassupervised(annotationtype:))*