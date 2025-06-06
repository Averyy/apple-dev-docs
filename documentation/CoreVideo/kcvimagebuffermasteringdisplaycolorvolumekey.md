# kCVImageBufferMasteringDisplayColorVolumeKey

**Framework**: Core Video  
**Kind**: var

A key to the mastering display color volume.

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
let kCVImageBufferMasteringDisplayColorVolumeKey: CFString
```

#### Discussion

The value for this key is 44 bytes, of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). It contains big-endian data to match the payload of ISO/IEC 23008-2:2015(E), D.2.28 mastering display color volume in the supplemental enhancement information (SEI) message.

## See Also

- [let kCVImageBufferCGColorSpaceKey: CFString](kcvimagebuffercgcolorspacekey.md)
  A key to the color space of the image buffer.
- [let kCVImageBufferCleanApertureKey: CFString](kcvimagebuffercleanaperturekey.md)
  A key to the dictionary describing the clean aperture for the image buffer.
- [let kCVImageBufferPreferredCleanApertureKey: CFString](kcvimagebufferpreferredcleanaperturekey.md)
  A key to the dictionary describing the preferred clean aperture for the image buffer.
- [let kCVImageBufferFieldCountKey: CFString](kcvimagebufferfieldcountkey.md)
  A key to the field count for the image buffer.
- [let kCVImageBufferFieldDetailKey: CFString](kcvimagebufferfielddetailkey.md)
  A key to the field detail for an image buffer that indicates the order of interlaced video data in the image buffer.
- [let kCVImageBufferPixelAspectRatioKey: CFString](kcvimagebufferpixelaspectratiokey.md)
  A key to the dictionary describing the pixel aspect ratio for the image buffer.
- [let kCVImageBufferDisplayDimensionsKey: CFString](kcvimagebufferdisplaydimensionskey.md)
  A key to the dictionary describing the display dimensions for the image buffer.
- [let kCVImageBufferGammaLevelKey: CFString](kcvimagebuffergammalevelkey.md)
  A key to the gamma level for the image buffer.
- [let kCVImageBufferICCProfileKey: CFString](kcvimagebuffericcprofilekey.md)
  A key to the ICC color profile for the image buffer.
- [let kCVImageBufferYCbCrMatrixKey: CFString](kcvimagebufferycbcrmatrixkey.md)
  A key to the YCbCr to RGB color conversion matrix for the image buffer.
- [let kCVImageBufferColorPrimariesKey: CFString](kcvimagebuffercolorprimarieskey.md)
  A key to the color primaries gamut for the image buffer.
- [let kCVImageBufferTransferFunctionKey: CFString](kcvimagebuffertransferfunctionkey.md)
  A key to the transfer function for the image buffer.
- [let kCVImageBufferChromaLocationTopFieldKey: CFString](kcvimagebufferchromalocationtopfieldkey.md)
  A key to the location of chroma top field information in the image buffer.
- [let kCVImageBufferChromaLocationBottomFieldKey: CFString](kcvimagebufferchromalocationbottomfieldkey.md)
  A key to the location of chroma bottom field information in the image buffer.
- [let kCVImageBufferChromaSubsamplingKey: CFString](kcvimagebufferchromasubsamplingkey.md)
  A key to the original format of subsampled data in the image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebuffermasteringdisplaycolorvolumekey)*