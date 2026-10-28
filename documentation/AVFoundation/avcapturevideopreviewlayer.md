# AVCaptureVideoPreviewLayer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A Core Animation layer that displays video from a camera device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureVideoPreviewLayer
```

```objc
@interface AVCaptureVideoPreviewLayer : CALayer
```

## Mentions

- [Setting up a capture session](./setting-up-a-capture-session.md)

## Overview

Use this layer to provide a preview of the content the camera captures. A convenient way to use this class in iOS is to set it as the backing layer for a view as shown below.

```swift
class PreviewView: UIView {
    // Use a capture video preview layer as the view's backing layer.
    override class var layerClass: AnyClass {
        AVCaptureVideoPreviewLayer.self
    }
    
    var previewLayer: AVCaptureVideoPreviewLayer {
        layer as! AVCaptureVideoPreviewLayer
    }
    
    // Connect the layer to a capture session.
    var session: AVCaptureSession? {
        get { previewLayer.session }
        set { previewLayer.session = newValue }
    }
}
```

## Topics

### Creating a preview layer
- [init(session: AVCaptureSession)](./avcapturevideopreviewlayer/init%28session%29.md)
  Creates a layer to preview the visual output of a capture session.
- [init(sessionWithNoConnection: AVCaptureSession)](./avcapturevideopreviewlayer/init%28sessionwithnoconnection%29.md)
  Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.
- [+ layerWithSession:](./avcapturevideopreviewlayer/layerwithsession_.md)
  Returns a new layer to preview the visual output of a capture session.
- [+ layerWithSessionWithNoConnection:](./avcapturevideopreviewlayer/layerwithsessionwithnoconnection_.md)
  Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.
### Layer configuration
- [var isPreviewing: Bool](./avcapturevideopreviewlayer/ispreviewing.md)
  A Boolean value that indicates whether the layer is rendering video frames from its source.
- [var videoGravity: AVLayerVideoGravity](./avcapturevideopreviewlayer/videogravity.md)
  A value that indicates how the layer displays video content within its bounds.
### Configuring deferred start
- [var isDeferredStartSupported: Bool](./avcapturevideopreviewlayer/isdeferredstartsupported.md)
  A `BOOL` value that indicates whether the preview layer supports deferred start.
- [var isDeferredStartEnabled: Bool](./avcapturevideopreviewlayer/isdeferredstartenabled.md)
  A `BOOL` value that indicates whether to defer starting this preview layer.
### Session configuration
- [var session: AVCaptureSession?](./avcapturevideopreviewlayer/session.md)
  A capture session with visual output to preview.
- [var connection: AVCaptureConnection?](./avcapturevideopreviewlayer/connection.md)
  An object that describes the connection from the layer to a particular input port.
- [func setSessionWithNoConnection(AVCaptureSession)](./avcapturevideopreviewlayer/setsessionwithnoconnection%28_%29.md)
  Associates a session with the layer without automatically forming a connection to an eligible input port.
### Converting between coordinate spaces
- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](./avcapturevideopreviewlayer/layerpointconverted%28fromcapturedevicepoint%29.md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](./avcapturevideopreviewlayer/capturedevicepointconverted%28fromlayerpoint%29.md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](./avcapturevideopreviewlayer/layerrectconverted%28frommetadataoutputrect%29.md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](./avcapturevideopreviewlayer/metadataoutputrectconverted%28fromlayerrect%29.md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](./avcapturevideopreviewlayer/transformedmetadataobject%28for%29.md)
  Converts a metadata object’s visual properties to layer coordinates.
### Deprecated
- [Deprecated symbols](./avcapturevideopreviewlayer-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [CALayer](../QuartzCore/calayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Capture preview
- [class AVCaptureAudioPreviewOutput](./avcaptureaudiopreviewoutput.md)
  A capture output that provides a preview of the captured audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer)*