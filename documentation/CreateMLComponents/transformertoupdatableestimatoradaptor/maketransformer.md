# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method

Creates a default-initialized transformer suitable for incremental fitting.

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
func makeTransformer() -> Transformer
```

## See Also

- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Transformer](transformertoupdatableestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.
- [func update<InputSequence>(inout Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](transformertoupdatableestimatoradaptor/update(_:with:eventhandler:).md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/maketransformer())*