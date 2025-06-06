# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on a sequence of input sequences.

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
func applied<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> [Self.OutputSequence] where S : Sequence, Self.Input == S.Element.Feature, S.Element : TemporalSequence
```

#### Return Value

The outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: The transformer inputs.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer/applied(to:eventhandler:)-6ju6s)*