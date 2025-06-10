# SRSpeechMetrics.SessionFlags

**Framework**: SensorKit  
**Kind**: struct

Possible details about processing an audio stream.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct SessionFlags
```

#### Overview

Use these flags to determine whether audio processing went through the system voice processor.

## Topics

### Session flags
- [static var bypassVoiceProcessing: SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.struct/bypassvoiceprocessing.md)
  Audio processing bypasses the system voice processor.
### Creating session flags
- [init(rawValue: UInt)](srspeechmetrics/sessionflags-swift.struct/init(rawvalue:).md)
  Creates and returns a new structure with the specified value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var sessionIdentifier: String](srspeechmetrics/sessionidentifier.md)
  An identifier for the audio session.
- [var sessionFlags: SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.property.md)
  Details about the audio processing.
- [var timeSinceAudioStart: TimeInterval](srspeechmetrics/timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](srspeechmetrics/timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)*