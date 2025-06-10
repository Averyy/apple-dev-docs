# Capturing cinematic video

**Framework**: AVFoundation

Capture video with an adjustable depth of field and focus points.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 319: [`Capture cinematic video in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/319).

##### Configure the Sample Code Project

Because Simulator doesn’t have access to access device cameras, you’ll need to run this sample app on an iOS device with iOS 26 or later installed.

## See Also

- [Setting Up a Capture Session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../AVKit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md)
  Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: Detecting Barcodes and Faces](avcambarcode-detecting-barcodes-and-faces.md)
  Identify machine readable codes or faces by using the camera.
- [class AVCaptureSession](avcapturesession.md)
  An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [class AVCaptureMultiCamSession](avcapturemulticamsession.md)
  A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [class AVCaptureInput](avcaptureinput.md)
  An abstract superclass for objects that provide input data to a capture session.
- [class AVCaptureOutput](avcaptureoutput.md)
  An abstract superclass for objects that provide media output destinations for a capture session.
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capturing-cinematic-video)*