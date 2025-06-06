# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the composed transformation on a single input.

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
func applied(to input: ComposedTransformer<Inner, Outer>.Input, eventHandler: EventHandler? = nil) async throws -> ComposedTransformer<Inner, Outer>.Output
```

#### Return Value

An output produced by applying the transformer to the input.

## Parameters

- `input`: The transformer input.
- `eventHandler`: An event handler.

## See Also

- [ComposedTransformer.Input](composedtransformer/input.md)
  The input type.
- [ComposedTransformer.Intermediate](composedtransformer/intermediate.md)
  The intermediate type.
- [ComposedTransformer.Output](composedtransformer/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtransformer/applied(to:eventhandler:))*