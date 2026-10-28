# CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Sets the auxiliary data, such as mattes and depth information, that accompany the image.

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
func CGImageDestinationAddAuxiliaryDataInfo(_ idst: CGImageDestination, _ auxiliaryImageDataType: CFString, _ auxiliaryDataInfoDictionary: CFDictionary)
```

```c
extern void CGImageDestinationAddAuxiliaryDataInfo(CGImageDestinationRef idst, CFStringRef auxiliaryImageDataType, CFDictionaryRef auxiliaryDataInfoDictionary);
```

## Discussion

Call this method after you add an image to the image destination. This method adds the specified depth or matte information to the most recently added image.

## Parameters

- `idst`: The image destination to modify.
- `auxiliaryImageDataType`: The type of auxiliary information you want to add. For a list of possible values, see [Auxiliary Data Types](./individual-image-properties.md#Auxiliary-Data-Types).
- `auxiliaryDataInfoDictionary`: A dictionary that contains the [`kCGImageAuxiliaryDataInfoData`](./kcgimageauxiliarydatainfodata.md), [`kCGImageAuxiliaryDataInfoDataDescription`](./kcgimageauxiliarydatainfodatadescription.md), and [`kCGImageAuxiliaryDataInfoMetadata`](./kcgimageauxiliarydatainfometadata.md) keys. Use those keys to describe the depth or matte information.

## See Also

### Adding Metadata to the Image
- [func CGImageDestinationSetProperties(CGImageDestination, CFDictionary?)](./cgimagedestinationsetproperties%28_,_%29.md)
  Applies one or more properties to all images in an image destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationaddauxiliarydatainfo(_:_:_:))*