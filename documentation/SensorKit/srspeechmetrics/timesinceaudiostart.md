# timeSinceAudioStart

**Framework**: SensorKit  
**Kind**: property

The number of seconds since the start of the audio stream.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
var timeSinceAudioStart: TimeInterval { get }
```

#### Discussion

When an audio stream starts, such as a phone call, SensorKit collects samples periodically. Use this field to determine the order of the samples in the audio stream.

## See Also

- [var sessionIdentifier: String](srspeechmetrics/sessionidentifier.md)
  An identifier for the audio session.
- [var sessionFlags: SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.property.md)
  Details about the audio processing.
- [SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timestamp: Date](srspeechmetrics/timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)*