# currentTime

**Framework**: AVFAudio  
**Kind**: property

The time, in seconds, since the beginning of the recording.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var currentTime: TimeInterval { get }
```

#### Discussion

The value of this property is `0` when you call it on a stopped audio recorder.

## See Also

- [var deviceCurrentTime: TimeInterval](avaudiorecorder/devicecurrenttime.md)
  The time, in seconds, of the host audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/currenttime)*