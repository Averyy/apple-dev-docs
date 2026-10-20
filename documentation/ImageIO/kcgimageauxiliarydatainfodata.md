# kCGImageAuxiliaryDataInfoData

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kCGImageAuxiliaryDataInfoData;
```

#### Discussion

The value of this property is a [`CFData`](../CoreFoundation/cfdata.md). Use the [`kCGImagePropertyAuxiliaryDataType`](./kcgimagepropertyauxiliarydatatype.md) property to determine the format of this data.

## See Also

### Auxiliary Image Data
- [let kCGImagePropertyAuxiliaryData: CFString](./kcgimagepropertyauxiliarydata.md)
  An array of dictionaries that contain auxiliary data for the images.
- [let kCGImagePropertyAuxiliaryDataType: CFString](./kcgimagepropertyauxiliarydatatype.md)
  The type of the auxiliary data.
- [let kCGImageAuxiliaryDataInfoDataDescription: CFString](./kcgimageauxiliarydatainfodatadescription.md)
  A dictionary of keys that describe the auxiliary data.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](./kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimageauxiliarydatainfodata)*