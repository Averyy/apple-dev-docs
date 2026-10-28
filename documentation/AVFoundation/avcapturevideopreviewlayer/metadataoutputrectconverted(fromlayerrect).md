# metadataOutputRectConverted(fromLayerRect:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGRect) metadataOutputRectOfInterestForRect:(CGRect) rectInLayerCoordinates;
```

## Return Value

A rectangle in the metadata output’s coordinate system.

## Discussion

A metadata capture output’s [`rectOfInterest`](../avcapturemetadataoutput/rectofinterest.md) a [`CGRect`](../../CoreFoundation/cgrect.md) value where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image.

The system takes the layer’s frame size and its [`videoGravity`](./videogravity.md) into consideration when making the conversion.

## Parameters

- `rectInLayerCoordinates`: A rectangle in the [`AVCaptureVideoPreviewLayer`](../avcapturevideopreviewlayer.md) object’s coordinate system.

## See Also

### Converting between coordinate spaces
- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](./layerpointconverted%28fromcapturedevicepoint%29.md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func captureDevicePointConverted(fromLayerPoint: CGPoint) -> CGPoint](./capturedevicepointconverted%28fromlayerpoint%29.md)
  Converts a point from layer coordinates to the coordinate space of the capture device.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](./layerrectconverted%28frommetadataoutputrect%29.md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](./transformedmetadataobject%28for%29.md)
  Converts a metadata object’s visual properties to layer coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect:))*