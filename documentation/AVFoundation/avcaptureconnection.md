# AVCaptureConnection

**Framework**: AVFoundation  
**Kind**: class

An object that represents a connection from a capture input to a capture output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureConnection
```

#### Overview

Capture inputs have one or more input ports (instances of [`AVCaptureInput.Port`](avcaptureinput/port.md)). Capture outputs can accept data from one or more sources (for example, an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) object accepts both video and audio data).

You can add an `AVCaptureConnection` instance to a session using the [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method only if the [`canAddConnection(_:)`](avcapturesession/canaddconnection(_:).md) method returns [`true`](https://developer.apple.com/documentation/swift/true). When using the [`addInput(_:)`](avcapturesession/addinput(_:).md) or [`addOutput(_:)`](avcapturesession/addoutput(_:).md) method, the session forms connections automatically between all compatible inputs and outputs. You only need to add connections manually when adding an input or output with no connections. You can also use connections to enable or disable the flow of data from a given input or to a given output.

## Topics

### Creating a connection
- [init(inputPorts: [AVCaptureInput.Port], output: AVCaptureOutput)](avcaptureconnection/init(inputports:output:).md)
  Creates a capture connection that represents a connection between multiple input ports and an output.
- [init(inputPort: AVCaptureInput.Port, videoPreviewLayer: AVCaptureVideoPreviewLayer)](avcaptureconnection/init(inputport:videopreviewlayer:).md)
  Creates a capture connection that represents a connection between an input port and a video preview layer.
### Enabling a connection
- [var isEnabled: Bool](avcaptureconnection/isenabled.md)
  Turns the connection on and off.
- [var isActive: Bool](avcaptureconnection/isactive.md)
  Indicates whether the connection is active.
### Inspecting a connection
- [var inputPorts: [AVCaptureInput.Port]](avcaptureconnection/inputports.md)
  An array of the connection’s input ports.
- [var output: AVCaptureOutput?](avcaptureconnection/output.md)
  The connection’s output port, if applicable.
- [var videoPreviewLayer: AVCaptureVideoPreviewLayer?](avcaptureconnection/videopreviewlayer.md)
  The video preview layer associated with the connection.
- [var audioChannels: [AVCaptureAudioChannel]](avcaptureconnection/audiochannels.md)
  An array of audio channels that the connection provides.
### Rotating a video
- [func isVideoRotationAngleSupported(CGFloat) -> Bool](avcaptureconnection/isvideorotationanglesupported(_:).md)
  Returns a Boolean value that indicates whether the connection supports a rotation angle.
- [var videoRotationAngle: CGFloat](avcaptureconnection/videorotationangle.md)
  A rotation angle the connection applies to a video flowing through it.
### Mirroring a video
- [var isVideoMirroringSupported: Bool](avcaptureconnection/isvideomirroringsupported.md)
  A Boolean value that indicates whether the connection supports video mirroring.
- [var isVideoMirrored: Bool](avcaptureconnection/isvideomirrored.md)
  A Boolean value that indicates whether the connection horizontally flips the video flowing through it.
- [var automaticallyAdjustsVideoMirroring: Bool](avcaptureconnection/automaticallyadjustsvideomirroring.md)
  A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.
### Stabilizing video
- [var isVideoStabilizationSupported: Bool](avcaptureconnection/isvideostabilizationsupported.md)
  A Boolean value that indicates whether this connection supports video stabilization.
- [var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode](avcaptureconnection/activevideostabilizationmode.md)
  The connection’s current stabilization mode.
- [var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode](avcaptureconnection/preferredvideostabilizationmode.md)
  The stabilization mode that’s the most appropriate for a video connection.
### Delivering camera calibration settings
- [var isCameraIntrinsicMatrixDeliverySupported: Bool](avcaptureconnection/iscameraintrinsicmatrixdeliverysupported.md)
  A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.
- [var isCameraIntrinsicMatrixDeliveryEnabled: Bool](avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled.md)
  A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.
### Configuring a video’s frame rate
- [var isVideoMinFrameDurationSupported: Bool](avcaptureconnection/isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var videoMinFrameDuration: CMTime](avcaptureconnection/videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var isVideoMaxFrameDurationSupported: Bool](avcaptureconnection/isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.
- [var videoMaxFrameDuration: CMTime](avcaptureconnection/videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.
### Scaling a video
- [var videoMaxScaleAndCropFactor: CGFloat](avcaptureconnection/videomaxscaleandcropfactor.md)
  The connection’s maximum video scale and crop factor.
- [var videoScaleAndCropFactor: CGFloat](avcaptureconnection/videoscaleandcropfactor.md)
  The current scale and crop factor the video output uses.
### Interlacing video
- [var isVideoFieldModeSupported: Bool](avcaptureconnection/isvideofieldmodesupported.md)
  A Boolean value that indicates whether the connection supports setting a video field mode.
- [var videoFieldMode: AVVideoFieldMode](avcaptureconnection/videofieldmode.md)
  A setting that tells the connection how to interlace video flowing through it.
- [enum AVVideoFieldMode](avvideofieldmode.md)
  Constants that indicate which interlacing modes the connection applies to video flowing through it.
### Deprecated
- [var isVideoStabilizationEnabled: Bool](avcaptureconnection/isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](avcaptureconnection/enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](avcaptureconnection/isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [var videoOrientation: AVCaptureVideoOrientation](avcaptureconnection/videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.
- [enum AVCaptureVideoOrientation](avcapturevideoorientation.md)
  Constants indicating video orientation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting Up a Capture Session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../AVKit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Capturing cinematic video](capturing-cinematic-video.md)
  Capture video with an adjustable depth of field and focus points.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection)*