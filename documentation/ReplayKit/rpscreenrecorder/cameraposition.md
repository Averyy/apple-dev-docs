# cameraPosition

**Framework**: ReplayKit  
**Kind**: property

The camera position to use.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cameraPosition: RPCameraPosition { get set }
```

#### Discussion

The default value of this property is [`AVCaptureDevice.Position.front`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/Position-swift.enum/front). You can use this property for key-value observing.

## See Also

- [var isAvailable: Bool](rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](rpscreenrecorder/iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](rpscreenrecorder/camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [enum RPCameraPosition](rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/cameraposition)*