# AudioFeaturePrint.Input

**Framework**: Create ML Components  
**Kind**: typealias

The input type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias Input = AVAudioPCMBuffer
```

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> AudioFeaturePrint.FeatureSequence](audiofeatureprint/applied(to:eventhandler:).md)
  Extracts audio features from an a sequence of audio buffers
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](audiofeatureprint/applied(to:eventhandler:)-74d6e.md)
  Performs the transformation on a sequence of annotated input sequences.
- [AudioFeaturePrint.Output](audiofeatureprint/output.md)
  The output type.
- [AudioFeaturePrint.FeatureSequence](audiofeatureprint/featuresequence.md)
  An async sequence of audio buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/input)*