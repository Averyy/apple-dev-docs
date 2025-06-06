# prediction(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction on a sequence of annotated inputs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func prediction<S, Annotation>(from input: S, eventHandler: EventHandler? = nil) async throws -> [AnnotatedPrediction<Self.Output, Annotation>] where S : Sequence, S.Element == AnnotatedFeature<Self.Input, Annotation>
```

#### Return Value

Annotated predictions produced by applying the transformer to the inputs.

## Parameters

- `input`: A sequence of annotated inputs.
- `eventHandler`: An event handler.

## See Also

- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/callasfunction(_:eventhandler:)-1xy6d.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](transformer/callasfunction(_:eventhandler:)-477jv.md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](transformer/prediction(from:)-107lm.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](transformer/prediction(from:)-57fan.md)
  Performs a prediction from a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/prediction(from:eventhandler:))*