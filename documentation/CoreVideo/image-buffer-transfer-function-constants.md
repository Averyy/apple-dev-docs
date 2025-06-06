# Image Buffer Transfer Function Constants

**Framework**: Core Video

Constants that indicate the transfer function for the image buffer.

#### Overview

Use the [`kCVImageBufferTransferFunctionKey`](kcvimagebuffertransferfunctionkey.md) key to attach one of these values to the image buffer. The transfer function describes the tonality of an image for use in color matching operations, along with a color primaries gamut (See [`Image Buffer Color Primaries Constants`](image-buffer-color-primaries-constants.md) for more information.). Most apps should specify the [`kCVImageBufferTransferFunction_ITU_R_709_2`](kcvimagebuffertransferfunction_itu_r_709_2.md) transfer function.

## Topics

### Constants
- [let kCVImageBufferTransferFunction_ITU_R_709_2: CFString](kcvimagebuffertransferfunction_itu_r_709_2.md)
  A key to the transfer function for high-definition and standard-definition video.
- [let kCVImageBufferTransferFunction_SMPTE_240M_1995: CFString](kcvimagebuffertransferfunction_smpte_240m_1995.md)
  A key to the transfer function for HDTV interim video.
- [let kCVImageBufferTransferFunction_UseGamma: CFString](kcvimagebuffertransferfunction_usegamma.md)
  A key to the transfer function that’s defined by the gamma level value of the image buffer.
- [let kCVImageBufferTransferFunction_sRGB: CFString](kcvimagebuffertransferfunction_srgb.md)
- [let kCVImageBufferTransferFunction_ITU_R_2020: CFString](kcvimagebuffertransferfunction_itu_r_2020.md)
- [let kCVImageBufferTransferFunction_SMPTE_ST_428_1: CFString](kcvimagebuffertransferfunction_smpte_st_428_1.md)
- [let kCVImageBufferTransferFunction_ITU_R_2100_HLG: CFString](kcvimagebuffertransferfunction_itu_r_2100_hlg.md)
- [let kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ: CFString](kcvimagebuffertransferfunction_smpte_st_2084_pq.md)

## See Also

- [Image Buffer Attachment Keys](image-buffer-attachment-keys.md)
  Keys that describe the attachment types associated with image buffers.
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
- [Image Buffer Chroma Location Constants](image-buffer-chroma-location-constants.md)
  Constants that indicate locations for chroma samples in the image buffer.
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-transfer-function-constants)*