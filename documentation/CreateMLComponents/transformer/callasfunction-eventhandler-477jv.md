# callAsFunction(_:eventHandler:)

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
func callAsFunction<S>(_ input: S, eventHandler: EventHandler? = nil) async throws -> [Self.Output] where S : Sequence, Self.Input == S.Element
```

#### Return Value

The outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: The transformer inputs.
- `eventHandler`: An event handler.

## See Also

- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/callasfunction(_:eventhandler:)-1xy6d.md)
  Performs the transformation on a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](transformer/prediction(from:)-107lm.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](transformer/prediction(from:)-57fan.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/callasfunction(_:eventhandler:)-477jv)*