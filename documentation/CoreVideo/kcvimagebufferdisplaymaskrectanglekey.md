# kCVImageBufferDisplayMaskRectangleKey

**Framework**: Core Video  
**Kind**: var

Specifies the rectangular display area within the image.

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
let kCVImageBufferDisplayMaskRectangleKey: CFString
```

#### Discussion

Specify the left, width, top, and height metrics relative to a reference raster width and height scaled to the image buffer dimensions.

The value is a dictionary containing these keys for the raster rectangle:

- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey`](kcvimagebufferdisplaymaskrectangle_referencerasterwidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey`](kcvimagebufferdisplaymaskrectangle_referencerasterheightkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleLeftKey`](kcvimagebufferdisplaymaskrectangle_rectangleleftkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleWidthKey`](kcvimagebufferdisplaymaskrectangle_rectanglewidthkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleTopKey`](kcvimagebufferdisplaymaskrectangle_rectangletopkey.md)
- [`kCVImageBufferDisplayMaskRectangle_RectangleHeightKey`](kcvimagebufferdisplaymaskrectangle_rectangleheightkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglekey)*