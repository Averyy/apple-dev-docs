# Image Buffer Display Dimensions Keys

**Framework**: Core Video

Keys that describe the display dimensions of an image buffer.

#### Overview

Define these key-value pairs in a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) instance and use the [`kCVImageBufferDisplayDimensionsKey`](kcvimagebufferdisplaydimensionskey.md) key to attach it to the image buffer.

## Topics

### Constants
- [let kCVImageBufferDisplayWidthKey: CFString](kcvimagebufferdisplaywidthkey.md)
  A key to the display width of the image buffer.
- [let kCVImageBufferDisplayHeightKey: CFString](kcvimagebufferdisplayheightkey.md)
  A key to the display height of the image buffer.

## See Also

- [Image Buffer Attachment Keys](image-buffer-attachment-keys.md)
  Keys that describe the attachment types associated with image buffers.
- [Image Buffer Clean Aperture Keys](image-buffer-clean-aperture-keys.md)
  Keys that describe the clean aperture of an image buffer.
- [Image Buffer Pixel Aspect Ratio Keys](image-buffer-pixel-aspect-ratio-keys.md)
  Keys that describe the pixel aspect ratio of an image buffer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-display-dimensions-keys)*