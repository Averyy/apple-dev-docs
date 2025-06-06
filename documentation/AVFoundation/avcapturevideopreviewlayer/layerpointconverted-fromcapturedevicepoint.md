# layerPointConverted(fromCaptureDevicePoint:)

**Framework**: AVFoundation  
**Kind**: method

Converts a point from the coordinate space of the capture device to the coordinate space of the layer.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func layerPointConverted(fromCaptureDevicePoint captureDevicePointOfInterest: CGPoint) -> CGPoint
```

#### Return Value

A point in layer coordinates.

#### Discussion

A capture device’s [`focusPointOfInterest`](avcapturedevice/focuspointofinterest.md) and [`exposurePointOfInterest`](avcapturedevice/exposurepointofinterest.md) properties provide a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) value where `{0,0}` represents the top-left and `{1,1}` represents the bottom-right of the unrotated image.

The system takes the layer’s frame size and its [`videoGravity`](avcapturevideopreviewlayer/videogravity.md) into consideration when making the conversion.

## Parameters

- `captureDevicePointOfInterest`: A point in capture device coordinates to convert.

## See Also

- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:).md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:).md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect:).md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](avcapturevideopreviewlayer/transformedmetadataobject(for:).md)
  Converts a metadata object’s visual properties to layer coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerpointconverted(fromcapturedevicepoint:))*