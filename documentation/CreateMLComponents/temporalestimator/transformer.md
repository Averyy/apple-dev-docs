# Transformer

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Required**: Yes

The transformer type created by this estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
associatedtype Transformer : TemporalTransformer
```

## See Also

- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](temporalestimator/adaptedassupervised(annotationtype:).md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](temporalestimator/fitted(to:).md)
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](temporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/transformer)*