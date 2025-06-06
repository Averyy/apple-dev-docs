# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a transformer with a new sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func update<InputSequence>(_ transformer: inout UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, InputSequence.Element : TemporalSequence, Base.Transformer.Input == InputSequence.Element.Feature
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [UpdatableEstimatorToTemporalAdaptor.Input](updatableestimatortotemporaladaptor/input.md)
  The input type.
- [UpdatableEstimatorToTemporalAdaptor.Output](updatableestimatortotemporaladaptor/output.md)
  The output type.
- [UpdatableEstimatorToTemporalAdaptor.Transformer](updatableestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/update(_:with:eventhandler:))*