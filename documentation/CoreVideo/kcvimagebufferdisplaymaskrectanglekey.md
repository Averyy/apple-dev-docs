# kCVImageBufferDisplayMaskRectangleKey

**Framework**: Core Video  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
let kCVImageBufferDisplayMaskRectangleKey: CFString
```

#### Discussion

```None
Specifies the rectangular display area within the image. The left, width, top and height are specified relative to a reference raster width and height that should be scaled to the image buffer dimensions.
```

Value is a dictionary containing these keys for the raster rectangle: kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey kCVImageBufferDisplayMaskRectangle_RectangleLeftKey kCVImageBufferDisplayMaskRectangle_RectangleWidthKey kCVImageBufferDisplayMaskRectangle_RectangleTopKey kCVImageBufferDisplayMaskRectangle_RectangleHeightKey


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglekey)*