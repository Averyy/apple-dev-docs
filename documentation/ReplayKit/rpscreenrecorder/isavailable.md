# isAvailable

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the screen recorder is available for recording.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCContentSharingPicker isAvailable instead

## Declaration

```swift
var isAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAvailable) BOOL available;
```

## Discussion

When set to [`true`](../../Swift/true.md), the screen recorder is available for recording. Screen recording can be unavailable due to unsupported hardware, the user’s device displaying information over Airplay or through a TVOut session, or another app using the recorder.

## See Also

### Inspecting a Screen Recorder
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
- [var delegate: (any RPScreenRecorderDelegate)?](./delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](../rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/isavailable)*