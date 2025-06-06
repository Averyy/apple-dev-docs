# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the composed transformation on an input sequence.

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
func applied<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> ComposedTemporalTransformer<Inner, Outer>.OutputSequence where S : TemporalSequence, Inner.Input == S.Feature
```

#### Return Value

An async sequence produced by applying the transformation to the input.

## Parameters

- `input`: The input temporal sequence.
- `eventHandler`: An event handler.

## See Also

- [ComposedTemporalTransformer.Intermediate](composedtemporaltransformer/intermediate.md)
  The intermediate type.
- [ComposedTemporalTransformer.Input](composedtemporaltransformer/input.md)
  The input type.
- [ComposedTemporalTransformer.Output](composedtemporaltransformer/output.md)
  The output type.
- [ComposedTemporalTransformer.OutputSequence](composedtemporaltransformer/outputsequence.md)
  The output sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer/applied(to:eventhandler:))*