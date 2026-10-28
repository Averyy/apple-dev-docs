# sessionIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

An identifier for the audio session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var sessionIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * sessionIdentifier;
```

## Discussion

For example, this property is an identifier for a phone call or Siri utterance.

## See Also

### Getting session information
- [var sessionFlags: SRSpeechMetrics.SessionFlags](./sessionflags-swift.property.md)
  Details about the audio processing.
- [SRSpeechMetrics.SessionFlags](./sessionflags-swift.struct.md)
  Possible details about processing an audio stream.
- [var timeSinceAudioStart: TimeInterval](./timesinceaudiostart.md)
  The number of seconds since the start of the audio stream.
- [var timestamp: Date](./timestamp.md)
  The date and time when the speech occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)*