# cameraPosition

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The camera position to use.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCVideoEffectOutput cameraDevice instead

## Declaration

```swift
var cameraPosition: RPCameraPosition { get set }
```

```objc
@property (nonatomic) RPCameraPosition cameraPosition;
```

#### Discussion

The default value of this property is [`AVCaptureDevice.Position.front`](../../AVFoundation/avcapturedevice/position-swift.enum/front.md). You can use this property for key-value observing.

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
- [enum RPCameraPosition](../rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](./delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](../rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/cameraposition)*