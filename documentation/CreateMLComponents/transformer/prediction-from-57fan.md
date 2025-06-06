# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction from a single input.

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
func prediction<Label>(from input: Self.Input) async throws -> ClassificationDistribution<Label> where Label : Hashable, Self.Output == ClassificationDistribution<Label>
```

#### Return Value

A classification array.

## Parameters

- `input`: The input feature.

## See Also

- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/callasfunction(_:eventhandler:)-1xy6d.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](transformer/callasfunction(_:eventhandler:)-477jv.md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](transformer/prediction(from:)-107lm.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/prediction(from:)-57fan)*