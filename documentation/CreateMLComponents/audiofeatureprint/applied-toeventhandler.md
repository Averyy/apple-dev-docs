# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Extracts audio features from an a sequence of audio buffers

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied<S>(to input: S, eventHandler: EventHandler? = nil) throws -> AudioFeaturePrint.FeatureSequence where S : TemporalSequence, S.Feature == AVAudioPCMBuffer
```

#### Return Value

An async sequence of shaped arrays containing extracted features. Each shaped array has a shape of `[512]`.

#### Discussion

You can call this method multiple times to process multiple streams.

## Parameters

- `input`: An async sequence of audio buffers.
- `eventHandler`: An event handler.

## See Also

- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](audiofeatureprint/applied(to:eventhandler:)-74d6e.md)
  Performs the transformation on a sequence of annotated input sequences.
- [AudioFeaturePrint.Input](audiofeatureprint/input.md)
  The input type.
- [AudioFeaturePrint.Output](audiofeatureprint/output.md)
  The output type.
- [AudioFeaturePrint.FeatureSequence](audiofeatureprint/featuresequence.md)
  An async sequence of audio buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/applied(to:eventhandler:))*