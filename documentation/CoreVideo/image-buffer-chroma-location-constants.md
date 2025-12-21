# Image Buffer Chroma Location Constants

**Framework**: Core Video

Constants that indicate locations for chroma samples in the image buffer.

#### Overview

For progressive-scan image data, use the [`kCVImageBufferChromaLocationTopFieldKey`](kcvimagebufferchromalocationtopfieldkey.md) key to attach one of these values to the image buffer. For interlaced image data, attach values to the image buffer using the [`kCVImageBufferChromaLocationTopFieldKey`](kcvimagebufferchromalocationtopfieldkey.md) and [`kCVImageBufferChromaLocationBottomFieldKey`](kcvimagebufferchromalocationbottomfieldkey.md) keys.

## Topics

### Constants
- [let kCVImageBufferChromaLocation_Left: CFString](kcvimagebufferchromalocation_left.md)
  A key that indicates the chroma sample is horizontally co-sited with the left column of luma samples, but centered vertically.
- [let kCVImageBufferChromaLocation_Center: CFString](kcvimagebufferchromalocation_center.md)
  A key that indicates the chroma sample is fully centered.
- [let kCVImageBufferChromaLocation_TopLeft: CFString](kcvimagebufferchromalocation_topleft.md)
  A key that indicates the chroma sample is co-sited with the top-left luma sample.
- [let kCVImageBufferChromaLocation_Top: CFString](kcvimagebufferchromalocation_top.md)
  A key that indicates the chroma sample is horizontally centered, but is co-sited with the top row of luma samples.
- [let kCVImageBufferChromaLocation_BottomLeft: CFString](kcvimagebufferchromalocation_bottomleft.md)
  A key that indicates the chroma sample is co-sited with the bottom-left luma sample.
- [let kCVImageBufferChromaLocation_Bottom: CFString](kcvimagebufferchromalocation_bottom.md)
  A key that indicates the chroma sample is horizontally centered, but is co-sited with the bottom row of luma samples.
- [let kCVImageBufferChromaLocation_DV420: CFString](kcvimagebufferchromalocation_dv420.md)
  A key that indicates the Cr and Cb samples are alternatingly co-sited with the left luma samples of the same field.

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
- [Image Buffer Transfer Function Constants](image-buffer-transfer-function-constants.md)
  Constants that indicate the transfer function for the image buffer.
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.
- [Image Buffer Display Mask Rectangle Keys](image-buffer-display-mask-rectangle-keys.md)
  Keys that describe the display dimensions of an image buffer mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-chroma-location-constants)*