# Image Buffer Display Mask Rectangle Keys

**Framework**: Core Video

Keys that describe the display dimensions of an image buffer mask.

#### Overview

Use [`kCVImageBufferDisplayMaskRectangleKey`](kcvimagebufferdisplaymaskrectanglekey.md) to attach a dictionary value containing display mask information to the image buffer. [`kCVImageBufferDisplayMaskRectangleStereoLeftKey`](kcvimagebufferdisplaymaskrectanglestereoleftkey.md) and [`kCVImageBufferDisplayMaskRectangleStereoRightKey`](kcvimagebufferdisplaymaskrectanglestereorightkey.md) perform the same function for left- and right-eye stereo images.

## Topics

### Constants
- [let kCVImageBufferDisplayMaskRectangle_LeftEdgePointsKey: CFString](kcvimagebufferdisplaymaskrectangle_leftedgepointskey.md)
  Specifies inset points on the left vertical edge of the rectangle.
- [let kCVImageBufferDisplayMaskRectangle_RectangleHeightKey: CFString](kcvimagebufferdisplaymaskrectangle_rectangleheightkey.md)
  Specifies the height of the rectangle starting at the rectangle’s top offset toward the rectangle’s bottom edge.
- [let kCVImageBufferDisplayMaskRectangle_RectangleLeftKey: CFString](kcvimagebufferdisplaymaskrectangle_rectangleleftkey.md)
  Specifies the horizontal pixel offset of the rectangle from the left of the bounding raster.
- [let kCVImageBufferDisplayMaskRectangle_RectangleTopKey: CFString](kcvimagebufferdisplaymaskrectangle_rectangletopkey.md)
  Specifies the vertical pixel offset of the rectangle from the top of the bounding raster.
- [let kCVImageBufferDisplayMaskRectangle_RectangleWidthKey: CFString](kcvimagebufferdisplaymaskrectangle_rectanglewidthkey.md)
  Specifies the width of the rectangle starting at the rectangle’s left offset toward the rectangle’s right edge.
- [let kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey: CFString](kcvimagebufferdisplaymaskrectangle_referencerasterheightkey.md)
  Specifies the height in pixels of the 2D coordinate system to define the rectangle.
- [let kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey: CFString](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
  Specifies the width in pixels of the 2D coordinate system to define the rectangle.
- [let kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey: CFString](kcvimagebufferdisplaymaskrectangle_rightedgepointskey.md)
  Specifies inset points on the right vertical edge of the rectangle.

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
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/image-buffer-display-mask-rectangle-keys)*