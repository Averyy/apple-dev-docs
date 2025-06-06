# applyingExifOrientation(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a derivative depth data object by mirroring or rotating it to the specified orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

#### Return Value

A new, transformed depth data object.

#### Discussion

When applying simple 90-degree rotation or mirroring edits to media containing depth data, you may use this method to create a derivative copy of the depth in which the specified orientation is applied to both the underlying pixel map data and the camera calibration data. This method throws an exception if you pass an unrecognized `exifOrientation` value.

A depth data object does not contain orientation metadata; this method assumes the data is in the default [`CGImagePropertyOrientation.up`](https://developer.apple.com/documentation/ImageIO/CGImagePropertyOrientation/up) orientation and applies the transformation necessary to produce the orientation you specify.

## Parameters

- `exifOrientation`: The image orientation to apply to the depth data map.

## See Also

- [func converting(toDepthDataType: OSType) -> Self](avdepthdata/converting(todepthdatatype:).md)
  Returns a derivative depth data object by converting the depth data map to the specified data type.
- [var availableDepthDataTypes: [OSType]](avdepthdata/availabledepthdatatypes-3ifx1.md)
  The list of depth data formats to which you can convert this depth data.
- [func replacingDepthDataMap(with: CVPixelBuffer) throws -> Self](avdepthdata/replacingdepthdatamap(with:).md)
  Returns a derivative depth data object by replacing the depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/applyingexiforientation(_:))*