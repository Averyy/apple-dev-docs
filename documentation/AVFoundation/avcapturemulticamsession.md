# AVCaptureMultiCamSession

**Framework**: AVFoundation  
**Kind**: class

A capture session that supports simultaneous capture from multiple inputs of the same media type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
class AVCaptureMultiCamSession
```

#### Overview

The session preset for a multicamera session is always [`inputPriority`](avcapturesession/preset/inputpriority.md). Set each capture device’s [`activeFormat`](avcapturedevice/activeformat.md) value to the desired quality of service.

You can dynamically enable and disable this session’s individual camera inputs without interrupting capture preview. To stop an individual camera, disable all of its connections or connected ports. The camera then stops streaming data to save power and bandwidth. Other inputs that are streaming data through the session are unaffected.

> **Note**:  If your app only needs to capture from a single camera at a time, use [`AVCaptureSession`](avcapturesession.md) instead.

## Topics

### Determining multi-camera support
- [class var isMultiCamSupported: Bool](avcapturemulticamsession/ismulticamsupported.md)
  A Boolean value that indicates whether this device supports multi-camera sessions.
### Managing resources
- [var hardwareCost: Float](avcapturemulticamsession/hardwarecost.md)
  A value that indicates the percentage of the session’s available hardware budget currently in use.
- [var systemPressureCost: Float](avcapturemulticamsession/systempressurecost.md)
  A value that indicates the system pressure cost of the current session configuration.

## Relationships

### Inherits From
- [AVCaptureSession](avcapturesession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up a capture session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../AVKit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Capturing Cinematic video](capturing-cinematic-video.md)
  Capture video with an adjustable depth of field and focus points.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md)
  Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: detecting barcodes and faces](avcambarcode-detecting-barcodes-and-faces.md)
  Identify machine readable codes or faces by using the camera.
- [class AVCaptureSession](avcapturesession.md)
  An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [class AVCaptureInput](avcaptureinput.md)
  An abstract superclass for objects that provide input data to a capture session.
- [class AVCaptureOutput](avcaptureoutput.md)
  An abstract superclass for objects that provide media output destinations for a capture session.
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession)*