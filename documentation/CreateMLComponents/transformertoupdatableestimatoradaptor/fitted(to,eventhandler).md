# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Returns the pre-defined transformer.

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
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> Transformer where S : Sequence, Transformer.Input == S.Element
```

#### Return Value

The pre-defined transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func makeTransformer() -> Transformer](transformertoupdatableestimatoradaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](transformertoupdatableestimatoradaptor/update(_:with:eventhandler:).md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/fitted(to:eventhandler:))*