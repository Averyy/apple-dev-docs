# AudioFeaturePrint

**Framework**: Create ML Components  
**Kind**: struct

A stream transformer that extracts audio features from audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AudioFeaturePrint
```

## Topics

### Creating a transformer
- [init(windowDuration: TimeInterval, overlapFactor: Double)](audiofeatureprint/init(windowduration:overlapfactor:).md)
  Creates an audio feature print feature extractor.
### Getting the properties
- [let overlapFactor: Double](audiofeatureprint/overlapfactor.md)
  The overlap factor of the extractor.
- [let windowDuration: TimeInterval](audiofeatureprint/windowduration.md)
  The window duration of the extractor.
### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> AudioFeaturePrint.FeatureSequence](audiofeatureprint/applied(to:eventhandler:).md)
  Extracts audio features from an a sequence of audio buffers
- [AudioFeaturePrint.FeatureSequence](audiofeatureprint/featuresequence.md)
  An async sequence of audio buffers.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)

## See Also

- [struct AudioReader](audioreader.md)
  An audio file reader.
- [struct AudioConvertingTransformer](audioconvertingtransformer.md)
  A transformer for audio conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint)*