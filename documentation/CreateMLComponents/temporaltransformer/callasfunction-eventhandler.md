# callAsFunction(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on an input sequence.

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
func callAsFunction<S>(_ input: S, eventHandler: EventHandler? = nil) async throws -> Self.OutputSequence where S : TemporalSequence, Self.Input == S.Feature
```

#### Return Value

An async sequence produced by applying the transformation to the input.

## Parameters

- `input`: The input temporal sequence.
- `eventHandler`: An event handler.

## See Also

- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](temporaltransformer/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](temporaltransformer/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/callasfunction(_:eventhandler:))*