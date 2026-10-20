# AVCaptureDevice.MicrophoneMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureMicrophoneMode : NSInteger;
```

## Topics

### Microphone modes
- [AVCaptureDevice.MicrophoneMode.standard](./microphonemode/standard.md)
  A mode that processes microphone audio with standard voice DSP.
- [AVCaptureDevice.MicrophoneMode.wideSpectrum](./microphonemode/widespectrum.md)
  A mode that minimizes microphone audio processing to capture all sounds in the room.
- [AVCaptureDevice.MicrophoneMode.voiceIsolation](./microphonemode/voiceisolation.md)
  A mode that processes microphone audio to isolate the voice and attenuate other signals.
### Initializers
- [init?(rawValue: Int)](./microphonemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the microphone mode
- [class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode](./activemicrophonemode.md)
  The device’s active microphone mode.
- [class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode](./preferredmicrophonemode.md)
  The microphone mode that the user selects in Control Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/microphonemode)*