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

## Declaration

```swift
func fitted<InputSequence>(to input: InputSequence, eventHandler: EventHandler? = nil) async throws -> Transformer where InputSequence : Sequence, Transformer.Input == InputSequence.Element.Feature, InputSequence.Element : TemporalSequence
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoestimatoradaptor/fitted(to:eventhandler:))*