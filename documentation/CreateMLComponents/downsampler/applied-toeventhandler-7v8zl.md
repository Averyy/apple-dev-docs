# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on a sequence of annotated input sequences.

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
func applied<S, TS, Annotation>(to input: S, eventHandler: EventHandler? = nil) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>] where S : Sequence, TS : TemporalSequence, Self.Input == TS.Feature, S.Element == AnnotatedFeature<TS, Annotation>
```

#### Return Value

The annotated outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: A sequence of annotated sequences.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/applied(to:eventhandler:)-7v8zl)*