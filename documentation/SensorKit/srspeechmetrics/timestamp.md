# timestamp

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The date and time when the speech occurs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var timestamp: Date { get }
```

```objc
@property (nonatomic, strong, readonly) NSDate * timestamp;
```

## See Also

### Getting session information
- [var sessionIdentifier: String](./sessionidentifier.md)
  An identifier for the audio session.
- [var sessionFlags: SRSpeechMetrics.SessionFlags](./sessionflags-swift.property.md)
  Details about the audio processing.
- [SRSpeechMetrics.SessionFlags](./sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timeSinceAudioStart: TimeInterval](./timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)*