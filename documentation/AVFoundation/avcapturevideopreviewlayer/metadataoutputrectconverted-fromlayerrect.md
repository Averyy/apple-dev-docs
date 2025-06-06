# metadataOutputRectConverted(fromLayerRect:)

**Framework**: AVFoundation  
**Kind**: method

Converts a rectangle from layer coordinates to the coordinate space of the metadata output.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func metadataOutputRectConverted(fromLayerRect rectInLayerCoordinates: CGRect) -> CGRect
```

#### Return Value

A rectangle in the metadata output’s coordinate system.

#### Discussion

A metadata capture output’s [`rectOfInterest`](avcapturemetadataoutput/rectofinterest.md) a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) value where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image.

The system takes the layer’s frame size and its [`videoGravity`](avcapturevideopreviewlayer/videogravity.md) into consideration when making the conversion.

## Parameters

- `rectInLayerCoordinates`: A rectangle in the   object’s coordinate system.

## See Also

- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/layerpointconverted(fromcapturedevicepoint:).md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:).md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:).md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](avcapturevideopreviewlayer/transformedmetadataobject(for:).md)
  Converts a metadata object’s visual properties to layer coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect:))*