# Image Buffer Chroma Subsampling Constants

**Framework**: Core Video

Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.

#### Overview

Use the [`kCVImageBufferChromaSubsamplingKey`](kcvimagebufferchromasubsamplingkey.md) key to attach one of these values to the image buffer.

> **Note**:  To use thse constants, ensure that the image buffer data was converted to 4:2:2 format using simple pixel replication.

## Topics

### Constants
- [let kCVImageBufferChromaSubsampling_420: CFString](kcvimagebufferchromasubsampling_420.md)
  A key that indicates the original chroma-subsampled data used 4:2:0 formatting.
- [let kCVImageBufferChromaSubsampling_422: CFString](kcvimagebufferchromasubsampling_422.md)
  A key that indicates the original chroma-subsampled data used 4:2:2 formatting.
- [let kCVImageBufferChromaSubsampling_411: CFString](kcvimagebufferchromasubsampling_411.md)
  A key that indicates the original chroma-subsampled data used 4:1:1 formatting.

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
- [Image Buffer Chroma Location Constants](image-buffer-chroma-location-constants.md)
  Constants that indicate locations for chroma samples in the image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-chroma-subsampling-constants)*