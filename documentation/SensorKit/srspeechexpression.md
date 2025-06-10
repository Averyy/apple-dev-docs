# SRSpeechExpression

**Framework**: SensorKit  
**Kind**: class

An object that represents the metrics and voice analytics for a range of speech.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRSpeechExpression
```

#### Overview

Use the properties of this class to get the characteristics of the speech, such as the user’s confidence level and mood.

## Topics

### Getting speech metrics
- [var timeRange: CMTimeRange](srspeechexpression/timerange.md)
  The time range in the audio stream that the metrics and analytics apply to.
- [var version: String](srspeechexpression/version.md)
  The version of the algorithm that the system uses to generate the metrics and analytics.
### Getting speech analytics
- [var confidence: Double](srspeechexpression/confidence.md)
  The level of confidence of the speaker.
- [var mood: Double](srspeechexpression/mood.md)
  An indication of how slurry, tired, or exhausted the speaker sounds compared to normal speech.
- [var valence: Double](srspeechexpression/valence.md)
  The degree of positive or negative emotion or sentiment of the speaker.
- [var activation: Double](srspeechexpression/activation.md)
  The level of energy or activation of the speaker.
- [var dominance: Double](srspeechexpression/dominance.md)
  The degree of how strong or meek the speaker sounds.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SRSpeechMetrics](srspeechmetrics.md)
  An object that represents metrics about a range of speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechexpression)*