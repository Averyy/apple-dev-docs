# init(fromImageSourceAuxiliaryDataType:dictionaryRepresentation:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) semanticSegmentationMatteFromImageSourceAuxiliaryDataType:(CFStringRef) imageSourceAuxiliaryDataType dictionaryRepresentation:(NSDictionary *) imageSourceAuxiliaryDataInfoDictionary error:(NSError **) outError;
```

## Return Value

A new semantic segmentation matte instance, or `nil` if the auxiliary data info dictionary is malformed.

## Parameters

- `imageSourceAuxiliaryDataType`: The `kCGImageAuxiliaryDataType` constants corresponding to the semantic segmentation matte being created (see `CGImageProperties`).
- `imageSourceAuxiliaryDataInfoDictionary`: A dictionary of primitive semantic segmentation matte information obtained from [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](../../ImageIO/cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md).

## See Also

### Creating a segmentation matte
- [func replacingSemanticSegmentationMatte(with: CVPixelBuffer) throws -> Self](./replacingsemanticsegmentationmatte%28with%29.md)
  Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](./applyingexiforientation%28_%29.md)
  Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](./dictionaryrepresentation%28forauxiliarydatatype%29.md)
  Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:))*