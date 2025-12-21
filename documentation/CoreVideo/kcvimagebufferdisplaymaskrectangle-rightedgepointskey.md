# kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey

**Framework**: Core Video  
**Kind**: var

Specifies inset points on the right vertical edge of the rectangle.

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
let kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey: CFString
```

#### Discussion

The points are [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) of unsigned 16-bit integer [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) pairs alternating between inset X and inset Y. Inset X is an unsigned offset from the right edge (`0`) towards the left edge (width). Inset Y is an unsigned offset from the top edge (`0`) towards the bottom edge (height).

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
- [let kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey: CFString](kcvimagebufferdisplaymaskrectangle_referencerasterheightkey.md)
  Specifies the height in pixels of the 2D coordinate system to define the rectangle.
- [let kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey: CFString](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
  Specifies the width in pixels of the 2D coordinate system to define the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectangle_rightedgepointskey)*