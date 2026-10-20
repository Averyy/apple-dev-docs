# deviceCurrentTime

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The time, in seconds, of the host audio device.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var deviceCurrentTime: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval deviceCurrentTime;
```

#### Discussion

Use this property value to schedule audio recording using the [`record(atTime:)`](./record%28attime%29.md) and [`record(atTime:forDuration:)`](./record%28attime,forduration%29.md) methods.

## See Also

### Accessing recorder timing
- [var currentTime: TimeInterval](./currenttime.md)
  The time, in seconds, since the beginning of the recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/devicecurrenttime)*