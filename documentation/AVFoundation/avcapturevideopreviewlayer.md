# AVCaptureVideoPreviewLayer

**Framework**: AVFoundation  
**Kind**: class

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

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)

#### Overview

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

### Creating a Preview Layer
- [init(session: AVCaptureSession)](avcapturevideopreviewlayer/init(session:).md)
  Creates a layer to preview the visual output of a capture session.
- [init(sessionWithNoConnection: AVCaptureSession)](avcapturevideopreviewlayer/init(sessionwithnoconnection:).md)
  Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.
### Layer Configuration
- [var isPreviewing: Bool](avcapturevideopreviewlayer/ispreviewing.md)
  A Boolean value that indicates whether the layer is rendering video frames from its source.
- [var videoGravity: AVLayerVideoGravity](avcapturevideopreviewlayer/videogravity.md)
  A value that indicates how the layer displays video content within its bounds.
### Session Configuration
- [var session: AVCaptureSession?](avcapturevideopreviewlayer/session.md)
  A capture session with visual output to preview.
- [var connection: AVCaptureConnection?](avcapturevideopreviewlayer/connection.md)
  An object that describes the connection from the layer to a particular input port.
- [func setSessionWithNoConnection(AVCaptureSession)](avcapturevideopreviewlayer/setsessionwithnoconnection(_:).md)
  Associates a session with the layer without automatically forming a connection to an eligible input port.
### Converting Between Coordinate Spaces
- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/layerpointconverted(fromcapturedevicepoint:).md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:).md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:).md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect:).md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](avcapturevideopreviewlayer/transformedmetadataobject(for:).md)
  Converts a metadata object’s visual properties to layer coordinates.
### Deprecated
- [Deprecated Symbols](avcapturevideopreviewlayer-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var isDeferredStartEnabled: Bool](avcapturevideopreviewlayer/isdeferredstartenabled.md)
  A Boolean value that indicates whether to defer starting this preview layer.
- [var isDeferredStartSupported: Bool](avcapturevideopreviewlayer/isdeferredstartsupported.md)
  A Boolean value that indicates whether the preview layer supports deferred start.

## Relationships

### Inherits From
- [CALayer](../QuartzCore/CALayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/CAMediaTiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVCaptureAudioPreviewOutput](avcaptureaudiopreviewoutput.md)
  A capture output that provides a preview of the captured audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer)*