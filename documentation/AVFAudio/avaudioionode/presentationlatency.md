# presentationLatency

**Framework**: AVFAudio  
**Kind**: property

The presentation or hardware latency, applicable when rendering to or from an audio device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var presentationLatency: TimeInterval { get }
```

#### Discussion

This corresponds to `kAudioDevicePropertyLatency` and `kAudioStreamPropertyLatency`. For more information, see `AudioHardwareBase.h` in `CoreAudio.Framework`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionode/presentationlatency)*