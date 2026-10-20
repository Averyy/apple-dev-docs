# prediction(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

### Transforming and predicting
- [func callAsFunction(_:eventHandler:)](./callasfunction%28_,eventhandler%29.md)
  Performs the transformation on a single input.
- [func prediction(from:)](./prediction%28from%29.md)
  Performs a prediction from a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/prediction(from:eventhandler:))*