# kCGImageAuxiliaryDataInfoData

**Framework**: Image I/O  
**Kind**: var

The auxiliary data for the image.

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
let kCGImageAuxiliaryDataInfoData: CFString
```

#### Discussion

The value of this property is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). Use the [`kCGImagePropertyAuxiliaryDataType`](kcgimagepropertyauxiliarydatatype.md) property to determine the format of this data.

## See Also

- [let kCGImagePropertyAuxiliaryData: CFString](kcgimagepropertyauxiliarydata.md)
  An array of dictionaries that contain auxiliary data for the images.
- [let kCGImagePropertyAuxiliaryDataType: CFString](kcgimagepropertyauxiliarydatatype.md)
  The type of the auxiliary data.
- [let kCGImageAuxiliaryDataInfoDataDescription: CFString](kcgimageauxiliarydatainfodatadescription.md)
  A dictionary of keys that describe the auxiliary data.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimageauxiliarydatainfodata)*