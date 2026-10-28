# isCameraEnabled

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the camera is currently enabled.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCContentSharingPickerConfiguration showsCameraControl instead

## Declaration

```swift
var isCameraEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isCameraEnabled) BOOL cameraEnabled;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). Set this property to [`true`](../../Swift/true.md) to enable the camera. When the app runs in visionOS, the value in this property is [`false`](../../Swift/false.md) and assigning a new value has no effect.

You can use this property for key-value observing.

> **Note**:  In your app’s `Info.plist` file, you must set the `Privacy - Camera Usage Description` key with a string that describes how your app uses the camera footage.

## See Also

### Inspecting a Screen Recorder
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](./ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/iscameraenabled)*