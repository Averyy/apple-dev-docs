# sessionIdentifier

**Framework**: SensorKit  
**Kind**: property

An identifier for the audio session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var sessionIdentifier: String { get }
```

#### Discussion

For example, this property is an identifier for a phone call or Siri utterance.

## See Also

- [var sessionFlags: SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.property.md)
  Details about the audio processing.
- [SRSpeechMetrics.SessionFlags](srspeechmetrics/sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timeSinceAudioStart: TimeInterval](srspeechmetrics/timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](srspeechmetrics/timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)*