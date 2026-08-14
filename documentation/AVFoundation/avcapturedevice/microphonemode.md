# AVCaptureDevice.MicrophoneMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that define the available microphone modes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
enum MicrophoneMode
```

## Topics

### Microphone modes
- [AVCaptureDevice.MicrophoneMode.standard](avcapturedevice/microphonemode/standard.md)
  A mode that processes microphone audio with standard voice DSP.
- [AVCaptureDevice.MicrophoneMode.wideSpectrum](avcapturedevice/microphonemode/widespectrum.md)
  A mode that minimizes microphone audio processing to capture all sounds in the room.
- [AVCaptureDevice.MicrophoneMode.voiceIsolation](avcapturedevice/microphonemode/voiceisolation.md)
  A mode that processes microphone audio to isolate the voice and attenuate other signals.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/microphonemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode](avcapturedevice/activemicrophonemode.md)
  The device’s active microphone mode.
- [class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode](avcapturedevice/preferredmicrophonemode.md)
  The microphone mode that the user selects in Control Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/microphonemode)*