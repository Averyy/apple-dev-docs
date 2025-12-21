# kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey

**Framework**: Core Video  
**Kind**: var

Specifies the height in pixels of the 2D coordinate system to define the rectangle.

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
let kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey: CFString
```

#### Discussion

The `0,0` origin is the top-left corner. The raster height value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of an unsigned 16-bit integer. The value usually matches the height of the video or the output device.

## See Also

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
- [let kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey: CFString](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
  Specifies the width in pixels of the 2D coordinate system to define the rectangle.
- [let kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey: CFString](kcvimagebufferdisplaymaskrectangle_rightedgepointskey.md)
  Specifies inset points on the right vertical edge of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectangle_referencerasterheightkey)*