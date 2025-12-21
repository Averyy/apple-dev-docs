# Image Buffer Attachment Keys

**Framework**: Core Video

Keys that describe the attachment types associated with image buffers.

#### Overview

An image buffer associates its attachment keys in a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) instance. To read and write these image buffer attachments, use the [`CVBufferCopyAttachment(_:_:_:)`](cvbuffercopyattachment(_:_:_:).md) and [`CVBufferSetAttachment(_:_:_:_:)`](cvbuffersetattachment(_:_:_:_:).md) functions or other [`CVBuffer`](cvbuffer.md) functions. See the [`CVBuffer`](cvbuffer-nfm.md) topic group for additional information.

## Topics

### Constants
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
- [let kCVImageBufferAlphaChannelIsOpaque: CFString](kcvimagebufferalphachannelisopaque.md)
  A key to indicate whether the alpha channel is fully opaque.
- [let kCVImageBufferContentLightLevelInfoKey: CFString](kcvimagebuffercontentlightlevelinfokey.md)
  A key to the content light level information.
- [let kCVImageBufferMasteringDisplayColorVolumeKey: CFString](kcvimagebuffermasteringdisplaycolorvolumekey.md)
  A key to the mastering display color volume.

## See Also

- [Image Buffer Clean Aperture Keys](image-buffer-clean-aperture-keys.md)
  Keys that describe the clean aperture of an image buffer.
- [Image Buffer Pixel Aspect Ratio Keys](image-buffer-pixel-aspect-ratio-keys.md)
  Keys that describe the pixel aspect ratio of an image buffer.
- [Image Buffer Display Dimensions Keys](image-buffer-display-dimensions-keys.md)
  Keys that describe the display dimensions of an image buffer.
- [Image Buffer Field Detail Constants](image-buffer-field-detail-constants.md)
  Constants that indicate the field order of interlaced video in an image buffer.
- [Image Buffer YCbCr Matrix Constants](image-buffer-ycbcr-matrix-constants.md)
  Constants that indicate the type of conversion matrix Core Video uses when it converts image buffer data from the YCbCr color space to the RGB color space.
- [Image Buffer Color Primaries Constants](image-buffer-color-primaries-constants.md)
  Constants that indicate the color primaries gamut for the image buffer.
- [Image Buffer Transfer Function Constants](image-buffer-transfer-function-constants.md)
  Constants that indicate the transfer function for the image buffer.
- [Image Buffer Chroma Location Constants](image-buffer-chroma-location-constants.md)
  Constants that indicate locations for chroma samples in the image buffer.
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.
- [Image Buffer Display Mask Rectangle Keys](image-buffer-display-mask-rectangle-keys.md)
  Keys that describe the display dimensions of an image buffer mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-attachment-keys)*