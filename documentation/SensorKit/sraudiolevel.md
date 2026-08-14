# SRAudioLevel

**Framework**: SensorKit  
**Kind**: class

An object that represents the audio level for a range of speech.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRAudioLevel
```

#### Overview

Use the [`loudness`](sraudiolevel/loudness.md) property to get the value of the audio level.

## Topics

### Getting metrics
- [var timeRange: CMTimeRange](sraudiolevel/timerange.md)
  The time range in the audio stream that the level applies to.
- [var loudness: Double](sraudiolevel/loudness.md)
  The measure of the audio level in decibels.

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

- [var audioLevel: SRAudioLevel?](srspeechmetrics/audiolevel.md)
  The audio level of the speech.
- [var speechRecognition: SFSpeechRecognitionResult?](srspeechmetrics/speechrecognition.md)
  The partial or final results of the speech recognition request.
- [var soundClassification: SNClassificationResult?](srspeechmetrics/soundclassification.md)
  The highest-ranking classifications in the time range.
- [var speechExpression: SRSpeechExpression?](srspeechmetrics/speechexpression.md)
  The metrics and voice analytics for the range of speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/sraudiolevel)*