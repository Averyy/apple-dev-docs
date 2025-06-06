# update(_:with:)

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
func update<InputSequence, FeatureSequence>(_ transformer: inout Self.Transformer, with input: InputSequence) async throws where InputSequence : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Self.Annotation>, FeatureSequence.Feature == Self.Transformer.Input
```

## See Also

- [func makeTransformer() -> Self.Transformer](updatablesupervisedtemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatablesupervisedtemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator/update(_:with:))*