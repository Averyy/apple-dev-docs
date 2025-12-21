# Image Buffer YCbCr Matrix Constants

**Framework**: Core Video

Constants that indicate the type of conversion matrix Core Video uses when it converts image buffer data from the YCbCr color space to the RGB color space.

#### Overview

Use the [`kCVImageBufferYCbCrMatrixKey`](kcvimagebufferycbcrmatrixkey.md) key to attach one of these values to the image buffer.

## Topics

### Constants
- [let kCVImageBufferYCbCrMatrix_ITU_R_2020: CFString](kcvimagebufferycbcrmatrix_itu_r_2020.md)
- [let kCVImageBufferYCbCrMatrix_P3_D65: CFString](kcvimagebufferycbcrmatrix_p3_d65.md)
- [let kCVImageBufferYCbCrMatrix_ITU_R_709_2: CFString](kcvimagebufferycbcrmatrix_itu_r_709_2.md)
  A key to the conversion matrix for HDTV digital television images, that follows the ITU R 709 standard.
- [let kCVImageBufferYCbCrMatrix_ITU_R_601_4: CFString](kcvimagebufferycbcrmatrix_itu_r_601_4.md)
  A key to the conversion matrix for standard digital television images, that follows the ITU R 601 standard.
- [let kCVImageBufferYCbCrMatrix_SMPTE_240M_1995: CFString](kcvimagebufferycbcrmatrix_smpte_240m_1995.md)
  A key to the conversion matrix for 1920 x 1135 HDTV images, that follows the SMPTE 240M 1995 standard.
- [let kCVImageBufferYCbCrMatrix_DCI_P3: CFString](kcvimagebufferycbcrmatrix_dci_p3.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-ycbcr-matrix-constants)*