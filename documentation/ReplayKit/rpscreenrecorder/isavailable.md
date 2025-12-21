# isAvailable

**Framework**: ReplayKit  
**Kind**: property

A Boolean value that indicates whether the screen recorder is available for recording.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var isAvailable: Bool { get }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/Swift/true), the screen recorder is available for recording. Screen recording can be unavailable due to unsupported hardware, the user’s device displaying information over Airplay or through a TVOut session, or another app using the recorder.

## See Also

- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/isavailable)*