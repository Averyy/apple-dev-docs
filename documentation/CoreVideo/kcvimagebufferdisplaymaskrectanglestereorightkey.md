# kCVImageBufferDisplayMaskRectangleStereoRightKey

**Framework**: Core Video  
**Kind**: var

Specifies the rectangular display area within the right-eye view of stereo images, using the same keys as `kCVImageBufferDisplayMaskRectangleKey`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
let kCVImageBufferDisplayMaskRectangleStereoRightKey: CFString
```

#### Discussion

To address window violations in stereo video, the system supports points insetting the left and right edges of the rectangle through additional keys, allowing the description of the extended raster rectangle.

The value is a dictionary containing these keys for the extended raster rectangle:

- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey`](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey`](kcvimagebufferdisplaymaskrectangle_referencerasterheightkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleLeftKey`](kcvimagebufferdisplaymaskrectangle_rectangleleftkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleWidthKey`](kcvimagebufferdisplaymaskrectangle_rectanglewidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleTopKey`](kcvimagebufferdisplaymaskrectangle_rectangletopkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleHeightKey`](kcvimagebufferdisplaymaskrectangle_rectangleheightkey.md)
- [`kCVImageBufferDisplayMaskRectangle_LeftEdgePointsKey`](kcvimagebufferdisplaymaskrectangle_leftedgepointskey.md)
- [`kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey`](kcvimagebufferdisplaymaskrectangle_rightedgepointskey.md)

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
- [Image Buffer Display Mask Rectangle Keys](image-buffer-display-mask-rectangle-keys.md)
  Keys that describe the display dimensions of an image buffer mask.
- [let kCVImageBufferDisplayMaskRectangleKey: CFString](kcvimagebufferdisplaymaskrectanglekey.md)
  Specifies the rectangular display area within the image.
- [let kCVImageBufferDisplayMaskRectangleStereoLeftKey: CFString](kcvimagebufferdisplaymaskrectanglestereoleftkey.md)
  Specifies the rectangular display area within the left-eye view of stereo images, using the same keys as `kCVImageBufferDisplayMaskRectangleKey`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglestereorightkey)*