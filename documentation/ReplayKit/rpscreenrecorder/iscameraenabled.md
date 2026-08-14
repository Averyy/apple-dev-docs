# isCameraEnabled

**Framework**: ReplayKit  
**Kind**: property

A Boolean value that indicates whether the camera is currently enabled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isCameraEnabled: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to enable the camera. When the app runs in visionOS, the value in this property is [`false`](https://developer.apple.com/documentation/swift/false) and assigning a new value has no effect.

You can use this property for key-value observing.

> **Note**:  In your app’s `Info.plist` file, you must set the `Privacy - Camera Usage Description` key with a string that describes how your app uses the camera footage.

## See Also

- [var isAvailable: Bool](rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/iscameraenabled)*