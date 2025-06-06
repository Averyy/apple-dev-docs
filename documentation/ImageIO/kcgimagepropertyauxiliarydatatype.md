# kCGImagePropertyAuxiliaryDataType

**Framework**: Image I/O  
**Kind**: var

The type of the auxiliary data.

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
let kCGImagePropertyAuxiliaryDataType: CFString
```

#### Discussion

The value of this property is a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString). The value of this key might be [`kCGImageAuxiliaryDataTypeDisparity`](kcgimageauxiliarydatatypedisparity.md), [`kCGImageAuxiliaryDataTypeDepth`](kcgimageauxiliarydatatypedepth.md), or another auxiliary data type.

## See Also

- [let kCGImagePropertyAuxiliaryData: CFString](kcgimagepropertyauxiliarydata.md)
  An array of dictionaries that contain auxiliary data for the images.
- [let kCGImageAuxiliaryDataInfoData: CFString](kcgimageauxiliarydatainfodata.md)
  The auxiliary data for the image.
- [let kCGImageAuxiliaryDataInfoDataDescription: CFString](kcgimageauxiliarydatainfodatadescription.md)
  A dictionary of keys that describe the auxiliary data.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyauxiliarydatatype)*