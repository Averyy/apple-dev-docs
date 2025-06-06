# availableDepthDataTypes

**Framework**: AVFoundation  
**Kind**: property

The list of depth data formats to which you can convert this depth data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
var availableDepthDataTypes: [OSType] { get }
```

#### Discussion

Use the [`converting(toDepthDataType:)`](avdepthdata/converting(todepthdatatype:).md) method to obtain a converted depth data object using one of the types in this list.

## See Also

- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avdepthdata/applyingexiforientation(_:).md)
  Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [func converting(toDepthDataType: OSType) -> Self](avdepthdata/converting(todepthdatatype:).md)
  Returns a derivative depth data object by converting the depth data map to the specified data type.
- [func replacingDepthDataMap(with: CVPixelBuffer) throws -> Self](avdepthdata/replacingdepthdatamap(with:).md)
  Returns a derivative depth data object by replacing the depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/availabledepthdatatypes-3ifx1)*