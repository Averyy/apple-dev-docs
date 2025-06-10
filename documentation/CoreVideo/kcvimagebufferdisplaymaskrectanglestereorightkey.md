# kCVImageBufferDisplayMaskRectangleStereoRightKey

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
let kCVImageBufferDisplayMaskRectangleStereoRightKey: CFString
```

#### Discussion

```None
Specifies the rectangular display area within the right eye view of stereo images, using the same keys as with kCVImageBufferDisplayMaskRectangleKey. To address window violations in stereo video, points insetting the left and right edges of the rectangle are supported through additional keys, allowing the description of the "extended raster rectangle".
```

Value is a dictionary containing these keys for the extended raster rectangle: kCVImageBufferDisplayMaskRectangle_ReferenceRasterWidthKey kCVImageBufferDisplayMaskRectangle_ReferenceRasterHeightKey kCVImageBufferDisplayMaskRectangle_RectangleLeftKey kCVImageBufferDisplayMaskRectangle_RectangleWidthKey kCVImageBufferDisplayMaskRectangle_RectangleTopKey kCVImageBufferDisplayMaskRectangle_RectangleHeightKey kCVImageBufferDisplayMaskRectangle_LeftEdgePointsKey kCVImageBufferDisplayMaskRectangle_RightEdgePointsKey


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglestereorightkey)*