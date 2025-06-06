# replacingSemanticSegmentationMatte(with:)

**Framework**: AVFoundation  
**Kind**: method

Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.

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
func replacingSemanticSegmentationMatte(with pixelBuffer: CVPixelBuffer) throws -> Self
```

#### Return Value

A new semantic segmentation matte instance, or `nil` if the pixel buffer is malformed.

#### Discussion

When applying complex edits to media containing a semantic segmentation matte, you may create a derivative matte with arbitrary transforms applied to it. You can then use this method to create a new semantic segmentation matte instance.

## Parameters

- `pixelBuffer`: A pixel buffer containing a semantic segmentation matting image, represented as   with a   transfer function.

## See Also

- [convenience init(fromImageSourceAuxiliaryDataType: CFString, dictionaryRepresentation: [AnyHashable : Any]) throws](avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:).md)
  Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avsemanticsegmentationmatte/applyingexiforientation(_:).md)
  Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:))*