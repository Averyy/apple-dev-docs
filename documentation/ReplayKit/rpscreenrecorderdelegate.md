# RPScreenRecorderDelegate

**Framework**: ReplayKit  
**Kind**: protocol  
**Role**: Protocol

The protocol you implement to receive notifications from the screen recorder.

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
protocol RPScreenRecorderDelegate : NSObjectProtocol
```

```objc
@protocol RPScreenRecorderDelegate <NSObject>
```

## Overview

Use this class to respond to changes to the screen recorder, represented by an [`RPScreenRecorder`](./rpscreenrecorder.md) object.

## Topics

### Responding to Recording Changes
- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](./rpscreenrecorderdelegate/screenrecorder%28_,didstoprecordingwith,error%29.md)
  Indicates that the screen recording has stopped.
- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](./rpscreenrecorderdelegate/screenrecorderdidchangeavailability%28_%29.md)
  Indicates that the recorder has changed states between disabled and enabled.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](./rpscreenrecorderdelegate/screenrecorder%28_,didstoprecordingwitherror,previewviewcontroller%29.md)
  Indicates that the screen recording has stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Inspecting a Screen Recorder
- [var isAvailable: Bool](./rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](./rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](./rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](./rpscreenrecorder/iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](./rpscreenrecorder/camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [var cameraPosition: RPCameraPosition](./rpscreenrecorder/cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](./rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](./rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)*