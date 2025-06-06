# AVCaptureOutput

**Framework**: AVFoundation  
**Kind**: class

An abstract superclass for objects that provide media output destinations for a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureOutput
```

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)

#### Overview

This class provides an abstract interface to connect capture output destinations, such as files and streams, to a capture session.

A capture output can have multiple connections, one for each stream of media that it receives from a capture input. A capture output doesn’t have any connections when you create it. When you add it to a capture session, the session automatically forms connections between compatible inputs and outputs.

## Topics

### Accessing Connections
- [var connections: [AVCaptureConnection]](avcaptureoutput/connections.md)
  The capture output object’s connections.
- [func connection(with: AVMediaType) -> AVCaptureConnection?](avcaptureoutput/connection(with:).md)
  Returns the first connection with an input port of a specified media type.
- [AVCaptureOutput.DataDroppedReason](avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.
### Converting Between Coordinate Systems
- [func transformedMetadataObject(for: AVMetadataObject, connection: AVCaptureConnection) -> AVMetadataObject?](avcaptureoutput/transformedmetadataobject(for:connection:).md)
  Converts a metadata object’s visual properties to layer coordinates.
- [func metadataOutputRectConverted(fromOutputRect: CGRect) -> CGRect](avcaptureoutput/metadataoutputrectconverted(fromoutputrect:).md)
  Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.
- [func outputRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](avcaptureoutput/outputrectconverted(frommetadataoutputrect:).md)
  Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md)
- [AVCaptureAudioPreviewOutput](avcaptureaudiopreviewoutput.md)
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md)
- [AVCaptureFileOutput](avcapturefileoutput.md)
- [AVCaptureMetadataOutput](avcapturemetadataoutput.md)
- [AVCapturePhotoOutput](avcapturephotooutput.md)
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md)
- [AVCaptureVideoDataOutput](avcapturevideodataoutput.md)
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
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput)*