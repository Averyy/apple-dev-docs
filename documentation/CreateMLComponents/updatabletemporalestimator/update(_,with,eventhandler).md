# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

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
func update<InputSequence>(_ transformer: inout Self.Transformer, with input: InputSequence, eventHandler: EventHandler?) async throws where InputSequence : Sequence, InputSequence.Element : TemporalSequence, Self.Transformer.Input == InputSequence.Element.Feature
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func makeTransformer() -> Self.Transformer](updatabletemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](updatabletemporalestimator/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimator/update(_:with:eventhandler:))*