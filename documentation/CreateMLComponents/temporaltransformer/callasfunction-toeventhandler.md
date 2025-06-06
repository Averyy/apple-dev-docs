# callAsFunction(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on a sequence of inputs.

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
func callAsFunction<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> [Self.OutputSequence] where S : Sequence, Self.Input == S.Element.Feature, S.Element : TemporalSequence
```

#### Return Value

The outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: The transformer inputs.
- `eventHandler`: An event handler.

## See Also

- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](temporaltransformer/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/callasfunction(to:eventhandler:))*