# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs the transformation on a sequence of annotated inputs.

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
func applied<S, Annotation>(to input: S, eventHandler: EventHandler? = nil) async throws -> [AnnotatedFeature<Self.Output, Annotation>] where S : Sequence, S.Element == AnnotatedFeature<Self.Input, Annotation>
```

#### Return Value

The annotated outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: A sequence of annotated inputs.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/applied(to:eventhandler:)-gcy8)*