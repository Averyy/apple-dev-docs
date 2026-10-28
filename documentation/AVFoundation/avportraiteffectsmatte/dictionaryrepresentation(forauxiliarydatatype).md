# dictionaryRepresentation(forAuxiliaryDataType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

A dictionary of primitive map information used for writing an image file with a portrait effects matte.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

```objc
- (NSDictionary *) dictionaryRepresentationForAuxiliaryDataType:(NSString **) outAuxDataType;
```

## Return Value

A dictionary of primitive map information for [`CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)`](../../ImageIO/cgimagedestinationaddauxiliarydatainfo%28_,_,_%29.md).

## Parameters

- `outAuxDataType`: Must be [`kCGImageAuxiliaryDataTypePortraitEffectsMatte`](../../ImageIO/kcgimageauxiliarydatatypeportraiteffectsmatte.md).

## See Also

### Examining a Portrait Effects matte
- [Extracting Portrait Effects matte image data from a photo](../extracting-portrait-effects-matte-image-data-from-a-photo.md)
  Check for portrait effects matte metadata in existing images.
- [var mattingImage: CVPixelBuffer](./mattingimage.md)
  The portrait effects matte’s internal image, formatted as a pixel buffer.
- [var pixelFormatType: OSType](./pixelformattype.md)
  The pixel format type of this portrait effects matte’s internal image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:))*