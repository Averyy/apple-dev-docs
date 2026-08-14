# SFVoiceAnalytics

**Framework**: Speech  
**Kind**: class

A collection of vocal analysis metrics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFVoiceAnalytics
```

#### Overview

Use an [`SFAcousticFeature`](sfacousticfeature.md) object to access the `SFVoiceAnalytics` insights. Voice analytics include the following features:

- Use [`jitter`](sfvoiceanalytics/jitter.md) to measure how pitch varies in audio.
- Use [`shimmer`](sfvoiceanalytics/shimmer.md) to measure how amplitude varies in audio.
- Use [`pitch`](sfvoiceanalytics/pitch.md) to measure the highness and lowness of the tone.
- Use [`voicing`](sfvoiceanalytics/voicing.md) to identify voiced regions in speech.

These results are part of the [`SFTranscriptionSegment`](sftranscriptionsegment.md) object and are available when the system sends the [`isFinal`](sfspeechrecognitionresult/isfinal.md) flag.

## Topics

### Analyzing voice
- [class SFAcousticFeature](sfacousticfeature.md)
  The value of a voice analysis metric.
- [var voicing: SFAcousticFeature](sfvoiceanalytics/voicing.md)
  The likelihood of a voice in each frame of a transcription segment.
- [var pitch: SFAcousticFeature](sfvoiceanalytics/pitch.md)
  The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.
- [var jitter: SFAcousticFeature](sfvoiceanalytics/jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.
- [var shimmer: SFAcousticFeature](sfvoiceanalytics/shimmer.md)
  The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.
### Initializers
- [init?(coder: NSCoder)](sfvoiceanalytics/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class SFAcousticFeature](sfacousticfeature.md)
  The value of a voice analysis metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfvoiceanalytics)*