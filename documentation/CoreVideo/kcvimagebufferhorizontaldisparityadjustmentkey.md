# kCVImageBufferHorizontalDisparityAdjustmentKey

**Framework**: Core Video  
**Kind**: var

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
let kCVImageBufferHorizontalDisparityAdjustmentKey: CFString
```

#### Discussion

Indicates a relative shift of the left and right images, which changes the zero parallax plane.

The value encoded in normalized image space is a CFNumber holding a signed 32-bit integer measured over the range of -10000 to 10000 mapping to the uniform range [-1.0…1.0]. The interval of 0.0 to 1.0 or 0 to 10000 maps onto the stereo eye view image width. The negative interval 0.0 to -1.0 or 0 to -10000 similarly map onto the stereo eye view image width. The default value of 0 is inferred if this property is not set.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferhorizontaldisparityadjustmentkey)*