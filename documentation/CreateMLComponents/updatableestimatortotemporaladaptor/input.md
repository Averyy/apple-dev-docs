# UpdatableEstimatorToTemporalAdaptor.Input

**Framework**: Create ML Components  
**Kind**: typealias

The input type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias Input = Base.Transformer.Input
```

## See Also

- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatableestimatortotemporaladaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [UpdatableEstimatorToTemporalAdaptor.Output](updatableestimatortotemporaladaptor/output.md)
  The output type.
- [UpdatableEstimatorToTemporalAdaptor.Transformer](updatableestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/input)*