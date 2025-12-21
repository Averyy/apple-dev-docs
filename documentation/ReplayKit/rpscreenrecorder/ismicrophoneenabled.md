# isMicrophoneEnabled

**Framework**: ReplayKit  
**Kind**: property

A Boolean value that indicates whether the microphone is currently enabled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var isMicrophoneEnabled: Bool { get set }
```

## See Also

- [var isAvailable: Bool](rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isCameraEnabled: Bool](rpscreenrecorder/iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](rpscreenrecorder/camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [var cameraPosition: RPCameraPosition](rpscreenrecorder/cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/ismicrophoneenabled)*