# UpdatableSupervisedEstimatorToTemporalAdaptor.Output

**Framework**: Create ML Components  
**Kind**: typealias

The output type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias Output = Base.Transformer.Output
```

## See Also

- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](updatablesupervisedestimatortotemporaladaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](updatablesupervisedestimatortotemporaladaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func makeTransformer() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](updatablesupervisedestimatortotemporaladaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatablesupervisedestimatortotemporaladaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Annotation](updatablesupervisedestimatortotemporaladaptor/annotation.md)
  The annotation type.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Input](updatablesupervisedestimatortotemporaladaptor/input.md)
  The input type.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Transformer](updatablesupervisedestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor/output)*