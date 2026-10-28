# activeMicrophoneMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The device’s active microphone mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode { get }
```

```objc
@property (class, readonly) AVCaptureMicrophoneMode activeMicrophoneMode;
```

## Discussion

The value may differ from the value of the [`preferredMicrophoneMode`](./preferredmicrophonemode.md) property if the app’s active audio route doesn’t support the mode.

This property is key-value observable.

## See Also

### Inspecting the microphone mode
- [class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode](./preferredmicrophonemode.md)
  The microphone mode that the user selects in Control Center.
- [AVCaptureDevice.MicrophoneMode](./microphonemode.md)
  Constants that define the available microphone modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activemicrophonemode)*