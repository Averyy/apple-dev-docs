# kCGImageAuxiliaryDataInfoDataDescription

**Framework**: Image I/O  
**Kind**: var

A dictionary of keys that describe the auxiliary data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let kCGImageAuxiliaryDataInfoDataDescription: CFString
```

#### Discussion

The value of this property is a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary). The keys in this dictionary may include [`kCGImagePropertyWidth`](kcgimagepropertywidth.md), [`kCGImagePropertyHeight`](kcgimagepropertyheight.md), and [`kCGImagePropertyBytesPerRow`](kcgimagepropertybytesperrow.md).

## See Also

- [let kCGImagePropertyAuxiliaryData: CFString](kcgimagepropertyauxiliarydata.md)
  An array of dictionaries that contain auxiliary data for the images.
- [let kCGImagePropertyAuxiliaryDataType: CFString](kcgimagepropertyauxiliarydatatype.md)
  The type of the auxiliary data.
- [let kCGImageAuxiliaryDataInfoData: CFString](kcgimageauxiliarydatainfodata.md)
  The auxiliary data for the image.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimageauxiliarydatainfodatadescription)*