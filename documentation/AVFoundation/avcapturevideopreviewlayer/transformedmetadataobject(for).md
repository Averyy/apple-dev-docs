# transformedMetadataObject(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVMetadataObject *) transformedMetadataObjectForMetadataObject:(AVMetadataObject *) metadataObject;
```

#### Return Value

A metadata object with coordinates converted into layer coordinates, or `nil` if the  metadata object originates from an input source other than that of the preview layer.

#### Discussion

The system provides the metadata object’s bounds as a rectangle where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image. Face metadata objects also provide [`yawAngle`](../avmetadatafaceobject/yawangle.md) and [`rollAngle`](../avmetadatafaceobject/rollangle.md) values with respect to an unrotated picture.

The conversion takes orientation, mirroring, layer bounds and video gravity into consideration.

## Parameters

- `metadataObject`: The metadata object whose visual properties you want to convert. The metadata object must originate from the same [`AVCaptureInput`](../avcaptureinput.md) as the preview layer.

## See Also

### Converting between coordinate spaces
- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](./layerpointconverted%28fromcapturedevicepoint%29.md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](./capturedevicepointconverted%28fromlayerpoint%29.md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](./layerrectconverted%28frommetadataoutputrect%29.md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](./metadataoutputrectconverted%28fromlayerrect%29.md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/transformedmetadataobject(for:))*