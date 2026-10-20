# SFVoiceAnalytics

**Framework**: Speech  
**Kind**: class  
**Role**: Class

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

```objc
@interface SFVoiceAnalytics : NSObject
```

#### Overview

Use an [`SFAcousticFeature`](./sfacousticfeature.md) object to access the `SFVoiceAnalytics` insights. Voice analytics include the following features:

- Use [`jitter`](./sfvoiceanalytics/jitter.md) to measure how pitch varies in audio.
- Use [`shimmer`](./sfvoiceanalytics/shimmer.md) to measure how amplitude varies in audio.
- Use [`pitch`](./sfvoiceanalytics/pitch.md) to measure the highness and lowness of the tone.
- Use [`voicing`](./sfvoiceanalytics/voicing.md) to identify voiced regions in speech.

These results are part of the [`SFTranscriptionSegment`](./sftranscriptionsegment.md) object and are available when the system sends the [`isFinal`](./sfspeechrecognitionresult/isfinal.md) flag.

## Topics

### Analyzing voice
- [class SFAcousticFeature](./sfacousticfeature.md)
  The value of a voice analysis metric.
- [var voicing: SFAcousticFeature](./sfvoiceanalytics/voicing.md)
  The likelihood of a voice in each frame of a transcription segment.
- [var pitch: SFAcousticFeature](./sfvoiceanalytics/pitch.md)
  The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.
- [var jitter: SFAcousticFeature](./sfvoiceanalytics/jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.
- [var shimmer: SFAcousticFeature](./sfvoiceanalytics/shimmer.md)
  The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.
### Initializers
- [init?(coder: NSCoder)](./sfvoiceanalytics/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Voice analytics
- [class SFAcousticFeature](./sfacousticfeature.md)
  The value of a voice analysis metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfvoiceanalytics)*