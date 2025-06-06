# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction on a single input.

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
func prediction<S, Label>(from input: S) async throws -> Self.OutputSequence where S : TemporalSequence, Label : Hashable, Self.Input == S.Feature, Self.Output == ClassificationDistribution<Label>
```

#### Return Value

A classification array.

## Parameters

- `input`: The input feature.

## See Also

- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](temporaltransformer/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/prediction(from:))*