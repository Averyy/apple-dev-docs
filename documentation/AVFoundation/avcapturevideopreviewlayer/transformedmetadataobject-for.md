# transformedMetadataObject(for:)

**Framework**: AVFoundation  
**Kind**: method

Converts a metadata object’s visual properties to layer coordinates.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func transformedMetadataObject(for metadataObject: AVMetadataObject) -> AVMetadataObject?
```

#### Return Value

A metadata object with coordinates converted into layer coordinates, or `nil` if the  metadata object originates from an input source other than that of the preview layer.

#### Discussion

The system provides the metadata object’s bounds as a rectangle where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image. Face metadata objects also provide [`yawAngle`](avmetadatafaceobject/yawangle.md) and [`rollAngle`](avmetadatafaceobject/rollangle.md) values with respect to an unrotated picture.

The conversion takes orientation, mirroring, layer bounds and video gravity into consideration.

## Parameters

- `metadataObject`: The metadata object whose visual properties you want to convert. The metadata object must originate from the same   as the preview layer.

## See Also

- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/layerpointconverted(fromcapturedevicepoint:).md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:).md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:).md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect:).md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/transformedmetadataobject(for:))*