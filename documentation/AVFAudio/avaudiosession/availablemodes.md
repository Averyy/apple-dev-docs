# availableModes

**Framework**: AVFAudio  
**Kind**: property

The audio session modes available on the device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var availableModes: [AVAudioSession.Mode] { get }
```

#### Discussion

Not every device supports every audio session mode. For example, the [`videoRecording`](avaudiosession/mode-swift.struct/videorecording.md) mode isn’t available on a device that doesn’t support video recording.

Query this property to determine if the mode you’d like to use is available on the current device.

## See Also

- [var mode: AVAudioSession.Mode](avaudiosession/mode-swift.property.md)
  The current audio session’s mode.
- [AVAudioSession.Mode](avaudiosession/mode-swift.struct.md)
  Audio session mode identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availablemodes)*