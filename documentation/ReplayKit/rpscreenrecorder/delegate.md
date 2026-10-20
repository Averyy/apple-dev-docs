# delegate

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the screen recorder.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit instead

## Declaration

```swift
weak var delegate: (any RPScreenRecorderDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<RPScreenRecorderDelegate> delegate;
```

#### Discussion

Set the delegate to respond to changes by the recorder; for example, when the recording stops.

## See Also

### Inspecting a Screen Recorder
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](./ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](./iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](./camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [var cameraPosition: RPCameraPosition](./cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](../rpcameraposition.md)
  The position of the camera being accessed.
- [protocol RPScreenRecorderDelegate](../rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/delegate)*