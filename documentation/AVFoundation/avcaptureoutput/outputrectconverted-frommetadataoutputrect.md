# outputRectConverted(fromMetadataOutputRect:)

**Framework**: AVFoundation  
**Kind**: method

Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func outputRectConverted(fromMetadataOutputRect rectInMetadataOutputCoordinates: CGRect) -> CGRect
```

#### Return Value

A rectangle in the [`AVCaptureOutput`](avcaptureoutput.md) object’s coordinate system.

#### Discussion

The rectangle of interest for an [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object is in a coordinate system extending from `{0,0}` in the top-left to `{1,1}` in the bottom-right, relative to the device’s natural orientation. A capture output object uses a pixel coordinate space which you may zoom, rotate, or mirror.

## Parameters

- `rectInMetadataOutputCoordinates`: A rectangle in the   coordinate system.

## See Also

- [func transformedMetadataObject(for: AVMetadataObject, connection: AVCaptureConnection) -> AVMetadataObject?](avcaptureoutput/transformedmetadataobject(for:connection:).md)
  Converts a metadata object’s visual properties to layer coordinates.
- [func metadataOutputRectConverted(fromOutputRect: CGRect) -> CGRect](avcaptureoutput/metadataoutputrectconverted(fromoutputrect:).md)
  Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/outputrectconverted(frommetadataoutputrect:))*