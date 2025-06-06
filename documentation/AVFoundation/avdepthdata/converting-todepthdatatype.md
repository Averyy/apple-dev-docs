# converting(toDepthDataType:)

**Framework**: AVFoundation  
**Kind**: method

Returns a derivative depth data object by converting the depth data map to the specified data type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func converting(toDepthDataType depthDataType: OSType) -> Self
```

#### Return Value

A new, converted depth data object.

#### Discussion

This method raises an exception if you pass an invalid `depthDataType` value.

## Parameters

- `depthDataType`: The data type to convert to. This value must be one of the formats present in the   array.

## See Also

- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avdepthdata/applyingexiforientation(_:).md)
  Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [var availableDepthDataTypes: [OSType]](avdepthdata/availabledepthdatatypes-3ifx1.md)
  The list of depth data formats to which you can convert this depth data.
- [func replacingDepthDataMap(with: CVPixelBuffer) throws -> Self](avdepthdata/replacingdepthdatamap(with:).md)
  Returns a derivative depth data object by replacing the depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/converting(todepthdatatype:))*