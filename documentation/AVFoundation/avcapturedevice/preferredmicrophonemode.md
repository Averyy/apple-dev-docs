# preferredMicrophoneMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, readonly) AVCaptureMicrophoneMode preferredMicrophoneMode;
```

## Discussion

Use key-value observing to monitor the user’s microphone mode selection.

## See Also

### Inspecting the microphone mode
- [class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode](./activemicrophonemode.md)
  The device’s active microphone mode.
- [AVCaptureDevice.MicrophoneMode](./microphonemode.md)
  Constants that define the available microphone modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/preferredmicrophonemode)*