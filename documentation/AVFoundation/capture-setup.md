# Capture setup

**Framework**: Avfoundation

Configure built-in cameras and microphones, and external capture devices, for media capture.

#### Overview

The AVFoundation Capture subsystem provides a common high-level architecture for video, photo, and audio capture services in iOS and macOS. Use this system if you want to:

- Build a custom camera UI to integrate shooting photos or videos into your app’s user experience.
- Give users more direct control over photo and video capture, such as focus, exposure, and stabilization options.
- Produce different results than the system camera UI, such as RAW format photos, depth maps, or videos with custom timed metadata.
- Get live access to pixel or audio data streaming directly from a capture device.

> **Note**:  To instead let the user capture media with the system camera UI within your app, see [`UIImagePickerController`](https://developer.apple.com/documentation/UIKit/UIImagePickerController).

The main parts of the capture architecture are sessions, inputs, and outputs: Capture sessions connect one or more inputs to one or more outputs. Inputs are sources of media, including capture devices like the cameras and microphones built into an iOS device or Mac. Outputs acquire media from inputs to produce useful data, such as movie files written to disk or raw pixel buffers available for live processing.

![Block diagram of the basic capture session architecture: an AVCaptureSession acquires data from an AVCaptureDevice through AVCaptureDeviceInput, and provides data to one or more AVCaptureOutput objects.](https://docs-assets.developer.apple.com/published/9b0221d1660fd2379e731fce79dc3522/media-2970476%402x.png)

## Topics

### Essentials
- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)
  Prompt the user to authorize access to the camera, microphone, and photo library.
### Capture sessions
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
### Capture devices
- [Choosing a Capture Device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [class AVCaptureDevice](avcapturedevice.md)
  An object that represents a hardware or virtual capture device like a camera or microphone.
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.
### Capture preview
- [class AVCaptureVideoPreviewLayer](avcapturevideopreviewlayer.md)
  A Core Animation layer that displays video from a camera device.
- [class AVCaptureAudioPreviewOutput](avcaptureaudiopreviewoutput.md)
  A capture output that provides a preview of the captured audio.
### Continuity camera
- [Supporting Continuity Camera in your tvOS app](../AVKit/supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [Supporting Continuity Camera in your macOS app](supporting-continuity-camera-in-your-macos-app.md)
  Enable high-quality photo and video capture by using an iPhone camera as an external capture device.
- [class AVCaptureDeskViewApplication](avcapturedeskviewapplication.md)
  An object that programmatically presents Desk View.
### Capture controls
- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)
  Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [class AVCaptureControl](avcapturecontrol.md)
  An abstract base class for controls that interact with the camera system.
- [class AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)
  A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [class AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md)
  A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [class AVCaptureSlider](avcaptureslider.md)
  A slider control that selects a value from a bounded range.
- [class AVCaptureIndexPicker](avcaptureindexpicker.md)
  A control for selecting from a set of mutually exclusive values by index.

## See Also

- [Photo capture](photo-capture.md)
  Capture high-quality still images, Live Photos, and supporting photo data.
- [Audio and video capture](audio-and-video-capture.md)
  Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
- [Additional data capture](additional-data-capture.md)
  Capture additional data including depth and metadata, and synchronize capture from multiple outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation/capture-setup)*