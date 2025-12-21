# kCVImageBufferDisplayMaskRectangleStereoLeftKey

**Framework**: Core Video  
**Kind**: var

Specifies the rectangular display area within the left-eye view of stereo images, using the same keys as `kCVImageBufferDisplayMaskRectangleKey`.

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
let kCVImageBufferDisplayMaskRectangleStereoLeftKey: CFString
```

#### Discussion

To address window violations in stereo video, the system supports points insetting the left and right edges of the rectangle through additional keys, allowing the description of the extended raster rectangle.

Value is a dictionary containing these keys for the extended raster rectangle:

- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey`](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey`](kcvimagebufferdisplaymaskrectangle_referencerasterheightkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleLeftKey`](kcvimagebufferdisplaymaskrectangle_rectangleleftkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleWidthKey`](kcvimagebufferdisplaymaskrectangle_rectanglewidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleTopKey`](kcvimagebufferdisplaymaskrectangle_rectangletopkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleHeightKey`](kcvimagebufferdisplaymaskrectangle_rectangleheightkey.md)
- [`kCVImageBufferDisplayMaskRectangle_LeftEdgePointsKey`](kcvimagebufferdisplaymaskrectangle_leftedgepointskey.md)
- [`kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey`](kcvimagebufferdisplaymaskrectangle_rightedgepointskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglestereoleftkey)*