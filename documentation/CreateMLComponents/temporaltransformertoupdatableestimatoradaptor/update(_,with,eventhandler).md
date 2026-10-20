# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Does nothing since this estimator uses a pre-defined transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func update<InputSequence>(_ transformer: inout Transformer, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Transformer.Input == InputSequence.Element.Feature, InputSequence.Element : TemporalSequence
```

## See Also

### Fitting and updating
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Transformer](./fitted%28to,eventhandler%29.md)
  Returns the pre-defined transformer.
- [func makeTransformer() -> Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/update(_:with:eventhandler:))*