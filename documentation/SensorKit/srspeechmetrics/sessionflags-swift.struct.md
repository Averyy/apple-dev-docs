# SRSpeechMetrics.SessionFlags

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

Possible details about processing an audio stream.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct SessionFlags
```

```c
enum SRSpeechMetricsSessionFlags : NSUInteger;
```

#### Overview

Use these flags to determine whether audio processing went through the system voice processor.

## Topics

### Session flags
- [static var bypassVoiceProcessing: SRSpeechMetrics.SessionFlags](./sessionflags-swift.struct/bypassvoiceprocessing.md)
  Audio processing bypasses the system voice processor.
### Creating session flags
- [init(rawValue: UInt)](./sessionflags-swift.struct/init%28rawvalue%29.md)
  Creates and returns a new structure with the specified value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting session information
- [var sessionIdentifier: String](./sessionidentifier.md)
  An identifier for the audio session.
- [var sessionFlags: SRSpeechMetrics.SessionFlags](./sessionflags-swift.property.md)
  Details about the audio processing.
- [var timeSinceAudioStart: TimeInterval](./timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](./timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)*