# kCVImageBufferChromaLocationBottomFieldKey

**Framework**: Core Video  
**Kind**: var

A key to the location of chroma bottom field information in the image buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCVImageBufferChromaLocationBottomFieldKey: CFString
```

#### Discussion

The chroma location value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString). This key only applies to interlaced image data. See [`Image Buffer Chroma Location Constants`](image-buffer-chroma-location-constants.md) for more information.

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
- [let kCVImageBufferChromaSubsamplingKey: CFString](kcvimagebufferchromasubsamplingkey.md)
  A key to the original format of subsampled data in the image buffer.
- [let kCVImageBufferAlphaChannelIsOpaque: CFString](kcvimagebufferalphachannelisopaque.md)
  A key to indicate whether the alpha channel is fully opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocationbottomfieldkey)*