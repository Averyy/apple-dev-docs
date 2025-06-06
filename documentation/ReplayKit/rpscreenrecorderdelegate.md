# RPScreenRecorderDelegate

**Framework**: ReplayKit  
**Kind**: protocol

The protocol you implement to receive notifications from the screen recorder.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol RPScreenRecorderDelegate : NSObjectProtocol
```

#### Overview

Use this class to respond to changes to the screen recorder, represented by an [`RPScreenRecorder`](rpscreenrecorder.md) object.

## Topics

### Responding to Recording Changes
- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwith:error:).md)
  Indicates that the screen recording has stopped.
- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](rpscreenrecorderdelegate/screenrecorderdidchangeavailability(_:).md)
  Indicates that the recorder has changed states between disabled and enabled.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:).md)
  Indicates that the screen recording has stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [var cameraPosition: RPCameraPosition](rpscreenrecorder/cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)*