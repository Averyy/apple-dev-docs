# preferredMicrophoneMode

**Framework**: AVFoundation  
**Kind**: property

The microphone mode that the user selects in Control Center.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode { get }
```

#### Discussion

Use key-value observing to monitor the user’s microphone mode selection.

## See Also

- [class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode](avcapturedevice/activemicrophonemode.md)
  The device’s active microphone mode.
- [AVCaptureDevice.MicrophoneMode](avcapturedevice/microphonemode.md)
  Constants that define the available microphone modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/preferredmicrophonemode)*