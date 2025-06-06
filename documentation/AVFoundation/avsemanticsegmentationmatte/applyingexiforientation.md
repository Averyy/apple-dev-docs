# applyingExifOrientation(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a new semantic segmentation matte instance with the specified Exif orientation applied.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

#### Return Value

A new semantic segmentation matte instance.

#### Discussion

This method throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) if you pass an unrecognized `exifOrientation`.

## Parameters

- `exifOrientation`: A   value expressing how the matte should be rotated or mirrored.

## See Also

- [convenience init(fromImageSourceAuxiliaryDataType: CFString, dictionaryRepresentation: [AnyHashable : Any]) throws](avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:).md)
  Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [func replacingSemanticSegmentationMatte(with: CVPixelBuffer) throws -> Self](avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:).md)
  Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/applyingexiforientation(_:))*