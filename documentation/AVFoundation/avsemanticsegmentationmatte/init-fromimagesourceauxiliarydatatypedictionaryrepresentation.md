# init(fromImageSourceAuxiliaryDataType:dictionaryRepresentation:)

**Framework**: AVFoundation  
**Kind**: init

Returns a new semantic segmentation matte instance from auxiliary image information in an image file.

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
convenience init(fromImageSourceAuxiliaryDataType imageSourceAuxiliaryDataType: CFString, dictionaryRepresentation imageSourceAuxiliaryDataInfoDictionary: [AnyHashable : Any]) throws
```

#### Return Value

A new semantic segmentation matte instance, or `nil` if the auxiliary data info dictionary is malformed.

## Parameters

- `imageSourceAuxiliaryDataType`: The   constants corresponding to the semantic segmentation matte being created (see  ).
- `imageSourceAuxiliaryDataInfoDictionary`: A dictionary of primitive semantic segmentation matte information obtained from  .

## See Also

- [func replacingSemanticSegmentationMatte(with: CVPixelBuffer) throws -> Self](avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:).md)
  Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avsemanticsegmentationmatte/applyingexiforientation(_:).md)
  Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:))*