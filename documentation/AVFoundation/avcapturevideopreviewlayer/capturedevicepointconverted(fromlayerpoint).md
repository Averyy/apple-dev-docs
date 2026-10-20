# captureDevicePointConverted(fromLayerPoint:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts a point from layer coordinates to the coordinate space of the capture device.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func captureDevicePointConverted(fromLayerPoint pointInLayer: CGPoint) -> CGPoint
```

```objc
- (CGPoint) captureDevicePointOfInterestForPoint:(CGPoint) pointInLayer;
```

#### Return Value

A point in capture device coordinates.

#### Discussion

A capture device’s [`focusPointOfInterest`](../avcapturedevice/focuspointofinterest.md) and [`exposurePointOfInterest`](../avcapturedevice/exposurepointofinterest.md) properties provide a [`CGPoint`](../../CoreFoundation/cgpoint.md) value where `{0,0}` represents the top-left and `{1,1}` represents the bottom-right of the unrotated image.

The conversion performed by this method takes the layer’s frame size and its [`videoGravity`](./videogravity.md) into consideration.

## Parameters

- `pointInLayer`: A point in layer coordinates to convert.

## See Also

### Converting between coordinate spaces
- [func layerPointConverted(fromCaptureDevicePoint: CGPoint) -> CGPoint](./layerpointconverted%28fromcapturedevicepoint%29.md)
  Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [func layerRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](./layerrectconverted%28frommetadataoutputrect%29.md)
  Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [func metadataOutputRectConverted(fromLayerRect: CGRect) -> CGRect](./metadataoutputrectconverted%28fromlayerrect%29.md)
  Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [func transformedMetadataObject(for: AVMetadataObject) -> AVMetadataObject?](./transformedmetadataobject%28for%29.md)
  Converts a metadata object’s visual properties to layer coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:))*