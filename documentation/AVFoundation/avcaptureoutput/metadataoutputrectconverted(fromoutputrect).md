# metadataOutputRectConverted(fromOutputRect:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func metadataOutputRectConverted(fromOutputRect rectInOutputCoordinates: CGRect) -> CGRect
```

```objc
- (CGRect) metadataOutputRectOfInterestForRect:(CGRect) rectInOutputCoordinates;
```

## Return Value

A rectangle in the [`AVCaptureMetadataOutput`](../avcapturemetadataoutput.md) coordinate system.

## Discussion

An [`AVCaptureMetadataOutput`](../avcapturemetadataoutput.md) object expresses its [`rectOfInterest`](../avcapturemetadataoutput/rectofinterest.md) as a [`CGRect`](../../CoreFoundation/cgrect.md) where 0,0 represents the top-left of the picture area, and 1,1 represents the bottom-right on an unrotated picture. This convenience method converts a rectangle in the coordinate space of the output to a rectangle of interest in the coordinate space of a metadata output whose capture device provides input to the output. The conversion takes orientation, mirroring, and scaling into consideration.

See [`transformedMetadataObject(for:connection:)`](./transformedmetadataobject%28for,connection%29.md) for a full discussion of how the system applies orientation and mirroring to sample buffers passing through the output.

## Parameters

- `rectInOutputCoordinates`: A rectangle in the [`AVCaptureOutput`](../avcaptureoutput.md) object’s coordinate system.

## See Also

### Converting between coordinate systems
- [func transformedMetadataObject(for: AVMetadataObject, connection: AVCaptureConnection) -> AVMetadataObject?](./transformedmetadataobject%28for,connection%29.md)
  Converts a metadata object’s visual properties to layer coordinates.
- [func outputRectConverted(fromMetadataOutputRect: CGRect) -> CGRect](./outputrectconverted%28frommetadataoutputrect%29.md)
  Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/metadataoutputrectconverted(fromoutputrect:))*