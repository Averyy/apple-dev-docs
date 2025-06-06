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
func fitted<InputSequence, FeatureSequence>(to input: InputSequence) async throws -> Self.Transformer where InputSequence : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Self.Annotation>, FeatureSequence.Feature == Self.Transformer.Input
```

## See Also

- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:validateon:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [associatedtype Annotation : Equatable, Sendable](supervisedtemporalestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : TemporalTransformer](supervisedtemporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/fitted(to:))*