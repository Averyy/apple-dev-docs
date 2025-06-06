# fitted(to:)

**Framework**: Create ML Components  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<InputSequence>(to input: InputSequence) async throws -> Self.Transformer where InputSequence : Sequence, InputSequence.Element : TemporalSequence, Self.Transformer.Input == InputSequence.Element.Feature
```

## See Also

- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](temporalestimator/adaptedassupervised(annotationtype:).md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](temporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [associatedtype Transformer : TemporalTransformer](temporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/fitted(to:))*