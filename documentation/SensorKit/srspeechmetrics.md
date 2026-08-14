# SRSpeechMetrics

**Framework**: SensorKit  
**Kind**: class

An object that represents metrics about a range of speech.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRSpeechMetrics
```

#### Overview

To get the audio level, use the [`audioLevel`](srspeechmetrics/audiolevel.md) property. Otherwise, use the [`speechRecognition`](srspeechmetrics/speechrecognition.md), [`soundClassification`](srspeechmetrics/soundclassification.md), and [`speechExpression`](srspeechmetrics/speechexpression.md) properties to get characteristics of the speech.

The [`siriSpeechMetrics`](srsensor/sirispeechmetrics.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Getting session information
- [var sessionIdentifier: String](srspeechmetrics/sessionidentifier.md)
  An identifier for the audio session.
- [var sessionFlags: SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.property.md)
  Details about the audio processing.
- [SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timeSinceAudioStart: TimeInterval](srspeechmetrics/timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](srspeechmetrics/timestamp.md)
  The date and time when the speech occurs.
### Getting speech metrics and analytics
- [var audioLevel: SRAudioLevel?](srspeechmetrics/audiolevel.md)
  The audio level of the speech.
- [class SRAudioLevel](sraudiolevel.md)
  An object that represents the audio level for a range of speech.
- [var speechRecognition: SFSpeechRecognitionResult?](srspeechmetrics/speechrecognition.md)
  The partial or final results of the speech recognition request.
- [var soundClassification: SNClassificationResult?](srspeechmetrics/soundclassification.md)
  The highest-ranking classifications in the time range.
- [var speechExpression: SRSpeechExpression?](srspeechmetrics/speechexpression.md)
  The metrics and voice analytics for the range of speech.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class SRSpeechExpression](srspeechexpression.md)
  An object that represents the metrics and voice analytics for a range of speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)*