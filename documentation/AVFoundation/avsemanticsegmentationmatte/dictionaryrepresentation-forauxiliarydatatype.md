# dictionaryRepresentation(forAuxiliaryDataType:)

**Framework**: AVFoundation  
**Kind**: method

Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.

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
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

#### Return Value

A dictionary of `CGImageDestination`-compatible semantic segmentation matte information, or `nil` if the auxiliary data type is unsupported.

## Parameters

- `outAuxDataType`: On output, the auxiliary data type to be used when calling the ImageIO framework’s   function. Currently supported auxiliary data types are enumerated in  .

## See Also

- [convenience init(fromImageSourceAuxiliaryDataType: CFString, dictionaryRepresentation: [AnyHashable : Any]) throws](avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:).md)
  Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [func replacingSemanticSegmentationMatte(with: CVPixelBuffer) throws -> Self](avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:).md)
  Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avsemanticsegmentationmatte/applyingexiforientation(_:).md)
  Returns a new semantic segmentation matte instance with the specified Exif orientation applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:))*