# callAsFunction(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs the transformation on a single input.

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
func callAsFunction(_ input: Self.Input, eventHandler: EventHandler? = nil) async throws -> Self.Output
```

**Other overloads**:

```swift
func callAsFunction<S>(_ input: S, eventHandler: EventHandler? = nil) async throws -> [Self.Output] where S : Sequence, Self.Input == S.Element
```

## Return Value

An output produced by applying the transformer to the input.

## Parameters

- `input`: The transformer input.
- `eventHandler`: An event handler.

## See Also

### Transforming and predicting
- [func prediction(from:)](./prediction%28from%29.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](./prediction%28from,eventhandler%29.md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/callasfunction(_:eventhandler:))*