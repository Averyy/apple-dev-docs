# sessionFlags

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

Details about the audio processing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var sessionFlags: SRSpeechMetrics.SessionFlags { get }
```

```objc
@property (nonatomic, assign, readonly) SRSpeechMetricsSessionFlags sessionFlags;
```

## See Also

### Getting session information
- [var sessionIdentifier: String](./sessionidentifier.md)
  An identifier for the audio session.
- [SRSpeechMetrics.SessionFlags](./sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timeSinceAudioStart: TimeInterval](./timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](./timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)*