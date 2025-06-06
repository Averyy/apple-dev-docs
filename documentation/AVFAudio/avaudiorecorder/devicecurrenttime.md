# deviceCurrentTime

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

Use this property value to schedule audio recording using the [`record(atTime:)`](avaudiorecorder/record(attime:).md) and [`record(atTime:forDuration:)`](avaudiorecorder/record(attime:forduration:).md) methods.

## See Also

- [var currentTime: TimeInterval](avaudiorecorder/currenttime.md)
  The time, in seconds, since the beginning of the recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/devicecurrenttime)*