# kCGImagePropertyAuxiliaryData

**Framework**: Image I/O  
**Kind**: var

An array of dictionaries that contain auxiliary data for the images.

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
let kCGImagePropertyAuxiliaryData: CFString
```

#### Discussion

The value of this key is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). Each [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) in the array contains auxiliary data for one of the images in the file. Use the [`kCGImagePropertyAuxiliaryDataType`](kcgimagepropertyauxiliarydatatype.md) key to determine the type of data associated with the image.

## See Also

- [let kCGImagePropertyAuxiliaryDataType: CFString](kcgimagepropertyauxiliarydatatype.md)
  The type of the auxiliary data.
- [let kCGImageAuxiliaryDataInfoData: CFString](kcgimageauxiliarydatainfodata.md)
  The auxiliary data for the image.
- [let kCGImageAuxiliaryDataInfoDataDescription: CFString](kcgimageauxiliarydatainfodatadescription.md)
  A dictionary of keys that describe the auxiliary data.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyauxiliarydata)*