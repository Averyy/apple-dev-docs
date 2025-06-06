# Individual Image Properties

**Framework**: Image I/O

Properties that apply to an individual image in an image source.

#### Overview

Access these properties using the [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](cgimagesourcecopypropertiesatindex(_:_:_:).md) or [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](cgimagesourcecopyauxiliarydatainfoatindex(_:_:_:).md) function.

## Topics

### Image Size
- [let kCGImagePropertyHeight: CFString](kcgimagepropertyheight.md)
  The height of the image, in the image’s coordinate space.
- [let kCGImagePropertyWidth: CFString](kcgimagepropertywidth.md)
  The width of the image, in the image’s coordinate space.
- [let kCGImagePropertyBytesPerRow: CFString](kcgimagepropertybytesperrow.md)
  The total number of bytes in each row of the image.
### Auxiliary Data Types
- [let kCGImageAuxiliaryDataTypeDepth: CFString](kcgimageauxiliarydatatypedepth.md)
  The type for depth map information.
- [let kCGImageAuxiliaryDataTypeDisparity: CFString](kcgimageauxiliarydatatypedisparity.md)
  The type for image disparity information.
- [let kCGImageAuxiliaryDataTypeHDRGainMap: CFString](kcgimageauxiliarydatatypehdrgainmap.md)
  The type for High Dynamic Range (HDR) gain map information.
- [let kCGImageAuxiliaryDataTypePortraitEffectsMatte: CFString](kcgimageauxiliarydatatypeportraiteffectsmatte.md)
  The type for portrait effects matte information.
- [let kCGImageAuxiliaryDataTypeSemanticSegmentationGlassesMatte: CFString](kcgimageauxiliarydatatypesemanticsegmentationglassesmatte.md)
  The type for glasses matte informaton.
- [let kCGImageAuxiliaryDataTypeSemanticSegmentationHairMatte: CFString](kcgimageauxiliarydatatypesemanticsegmentationhairmatte.md)
  The type for hair matte information.
- [let kCGImageAuxiliaryDataTypeSemanticSegmentationSkinMatte: CFString](kcgimageauxiliarydatatypesemanticsegmentationskinmatte.md)
  The type for skin matte informaton.
- [let kCGImageAuxiliaryDataTypeSemanticSegmentationSkyMatte: CFString](kcgimageauxiliarydatatypesemanticsegmentationskymatte.md)
  The type for sky matte information.
- [let kCGImageAuxiliaryDataTypeSemanticSegmentationTeethMatte: CFString](kcgimageauxiliarydatatypesemanticsegmentationteethmatte.md)
  The type for teeth matte information.
### Auxiliary Image Data
- [let kCGImagePropertyAuxiliaryData: CFString](kcgimagepropertyauxiliarydata.md)
  An array of dictionaries that contain auxiliary data for the images.
- [let kCGImagePropertyAuxiliaryDataType: CFString](kcgimagepropertyauxiliarydatatype.md)
  The type of the auxiliary data.
- [let kCGImageAuxiliaryDataInfoData: CFString](kcgimageauxiliarydatainfodata.md)
  The auxiliary data for the image.
- [let kCGImageAuxiliaryDataInfoDataDescription: CFString](kcgimageauxiliarydatainfodatadescription.md)
  A dictionary of keys that describe the auxiliary data.
- [let kCGImageAuxiliaryDataInfoMetadata: CFString](kcgimageauxiliarydatainfometadata.md)
  The metadata for any auxiliary data.
### Open EXR Properties
- [let kCGImagePropertyOpenEXRDictionary: CFString](kcgimagepropertyopenexrdictionary.md)
  A dictionary of properties specific to the OpenEXR metadata standard.
- [let kCGImagePropertyOpenEXRAspectRatio: CFString](kcgimagepropertyopenexraspectratio.md)
  The aspect ratio of the image.

## See Also

- [let kCGImagePropertyImageCount: CFString](kcgimagepropertyimagecount.md)
  The number of images in the file.
- [let kCGImagePropertyIsIndexed: CFString](kcgimagepropertyisindexed.md)
  A Boolean value that indicates whether the image contains indexed pixel samples.
- [let kCGImagePropertyImages: CFString](kcgimagepropertyimages.md)
  An array of dictionaries, each of which contains metadata for one of the images in the file.
- [let kCGImagePropertyThumbnailImages: CFString](kcgimagepropertythumbnailimages.md)
- [let kCGImagePropertyPrimaryImage: CFString](kcgimagepropertyprimaryimage.md)
  The index of the primary image in the file.
- [let kCGImagePropertyIsFloat: CFString](kcgimagepropertyisfloat.md)
  A Boolean value that indicates whether the image contains floating-point pixel samples.
- [let kCGImagePropertyOrientation: CFString](kcgimagepropertyorientation.md)
  The intended display orientation of the image.
- [enum CGImagePropertyOrientation](cgimagepropertyorientation.md)
  A value describing the intended display orientation for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/individual-image-properties)*