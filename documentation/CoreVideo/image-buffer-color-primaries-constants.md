# Image Buffer Color Primaries Constants

**Framework**: Core Video

Constants that indicate the color primaries gamut for the image buffer.

#### Overview

Use the [`kCVImageBufferColorPrimariesKey`](kcvimagebuffercolorprimarieskey.md) key to attach one of these values to the image buffer. The color primaries gamut describes the rendering intent of an image, for use in color matching operations, along with a transfer function (See [`Image Buffer Transfer Function Constants`](image-buffer-transfer-function-constants.md) for more information.).

## Topics

### Constants
- [let kCVImageBufferColorPrimaries_ITU_R_709_2: CFString](kcvimagebuffercolorprimaries_itu_r_709_2.md)
  A key to the color primaries gamut for HD video.
- [let kCVImageBufferColorPrimaries_EBU_3213: CFString](kcvimagebuffercolorprimaries_ebu_3213.md)
  A key to the color primaries gamut for PAL video.
- [let kCVImageBufferColorPrimaries_SMPTE_C: CFString](kcvimagebuffercolorprimaries_smpte_c.md)
  A key to the color primaries gamut for standard-definition video.
- [let kCVImageBufferColorPrimaries_DCI_P3: CFString](kcvimagebuffercolorprimaries_dci_p3.md)
- [let kCVImageBufferColorPrimaries_ITU_R_2020: CFString](kcvimagebuffercolorprimaries_itu_r_2020.md)
- [let kCVImageBufferColorPrimaries_P3_D65: CFString](kcvimagebuffercolorprimaries_p3_d65.md)
- [let kCVImageBufferColorPrimaries_P22: CFString](kcvimagebuffercolorprimaries_p22.md)
  A key to the color primaries gamut for sRGB video.

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
- [Image Buffer Transfer Function Constants](image-buffer-transfer-function-constants.md)
  Constants that indicate the transfer function for the image buffer.
- [Image Buffer Chroma Location Constants](image-buffer-chroma-location-constants.md)
  Constants that indicate locations for chroma samples in the image buffer.
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.
- [Image Buffer Display Mask Rectangle Keys](image-buffer-display-mask-rectangle-keys.md)
  Keys that describe the display dimensions of an image buffer mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-color-primaries-constants)*