# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a transformer on an async sequence of examples.

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
func update<Input>(_ transformer: inout Self.Transformer, with input: Input, eventHandler: EventHandler? = nil) async throws where Input : AsyncSequence, Input.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```

#### Discussion

Note that the async sequence is collected before updating the transformer.

## Parameters

- `transformer`: A transformer to update.
- `input`: An async sequence of examples used for updating the transformer.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/update(_:with:eventhandler:)-w2v0)*