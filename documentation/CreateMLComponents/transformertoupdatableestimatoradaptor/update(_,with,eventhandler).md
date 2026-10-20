# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Does nothing since this estimator uses a pre-defined transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func update<InputSequence>(_ transformer: inout Transformer, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Transformer.Input == InputSequence.Element
```

## See Also

### Fitting and updating
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Transformer](./fitted%28to,eventhandler%29.md)
  Returns the pre-defined transformer.
- [func makeTransformer() -> Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/update(_:with:eventhandler:))*