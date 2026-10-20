# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

### Fitting and updating
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Transformer](./fitted%28to,eventhandler%29.md)
  Returns the pre-defined transformer.
- [func update<InputSequence>(inout Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/maketransformer())*