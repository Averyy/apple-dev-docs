# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Does nothing since this estimator uses a pre-defined transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func update<InputSequence>(_ transformer: inout Transformer, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Transformer.Input == InputSequence.Element.Feature, InputSequence.Element : TemporalSequence
```

## See Also

- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.
- [func makeTransformer() -> Transformer](temporaltransformertoupdatableestimatoradaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/update(_:with:eventhandler:))*