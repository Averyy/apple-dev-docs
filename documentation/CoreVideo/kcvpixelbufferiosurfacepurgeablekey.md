# kCVPixelBufferIOSurfacePurgeableKey

**Framework**: Core Video  
**Kind**: var

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 26.0+

## Declaration

```swift
let kCVPixelBufferIOSurfacePurgeableKey: CFString
```

#### Discussion

Key sets the IOSurface backed memory allocation for CVPixelBuffer as purgeable and non-volatile.

A purgeable IOSurface is capable of being switched between non-volatile, volatile and empty states using IOSurfaceSetPurgeable.  When in the volatile state, the OS is permitted to instantly change its state to empty and remove all its memory pages.  Clients should set the IOSurfaces to the non-volatile state while they are in use and the volatile state when their need and contents is optional/speculative and OK to discard in response to system memory demand.  See IOSurfaceSetPurgeable for more details.  This key is only effective for CVPixelBuffers that are backed by IOSurface.

## See Also

- [let kCVPixelBufferMemoryAllocatorKey: CFString](kcvpixelbuffermemoryallocatorkey.md)
  A key to the allocator that the system uses to create the pixel buffer.
- [let kCVPixelBufferPixelFormatTypeKey: CFString](kcvpixelbufferpixelformattypekey.md)
  A key to one or more pixel buffer format types.
- [let kCVPixelBufferWidthKey: CFString](kcvpixelbufferwidthkey.md)
  A key to the width of the pixel buffer.
- [let kCVPixelBufferHeightKey: CFString](kcvpixelbufferheightkey.md)
  A key to the height of the pixel buffer.
- [let kCVPixelBufferExtendedPixelsLeftKey: CFString](kcvpixelbufferextendedpixelsleftkey.md)
  A key to the number of pixels padding the left of the image.
- [let kCVPixelBufferExtendedPixelsTopKey: CFString](kcvpixelbufferextendedpixelstopkey.md)
  A key to the number of pixels padding the top of the image.
- [let kCVPixelBufferExtendedPixelsRightKey: CFString](kcvpixelbufferextendedpixelsrightkey.md)
  A key to the number of pixels padding the right of the image.
- [let kCVPixelBufferExtendedPixelsBottomKey: CFString](kcvpixelbufferextendedpixelsbottomkey.md)
  A key to the number of pixels padding the bottom of the image.
- [let kCVPixelBufferBytesPerRowAlignmentKey: CFString](kcvpixelbufferbytesperrowalignmentkey.md)
  A key to a number that specifies the alignment of number of bytes per row in the pixel buffer.
- [let kCVPixelBufferCGBitmapContextCompatibilityKey: CFString](kcvpixelbuffercgbitmapcontextcompatibilitykey.md)
  A key to a Boolean value that indicates whether the pixel buffer is compatible with Core Graphics bitmap contexts.
- [let kCVPixelBufferCGImageCompatibilityKey: CFString](kcvpixelbuffercgimagecompatibilitykey.md)
  A key to a Boolean value that indicates whether the pixel buffer is compatible with Core Graphics bitmap image types.
- [let kCVPixelBufferOpenGLCompatibilityKey: CFString](kcvpixelbufferopenglcompatibilitykey.md)
  A key to a Boolean value that indicates whether the pixel buffer is compatible with OpenGL contexts.
- [let kCVPixelBufferPlaneAlignmentKey: CFString](kcvpixelbufferplanealignmentkey.md)
  A key to a number that specifies the alignment of the planes in the pixel buffer.
- [let kCVPixelBufferIOSurfacePropertiesKey: CFString](kcvpixelbufferiosurfacepropertieskey.md)
  A key to the dictionary containing optional properties for the IOSurface framework.
- [let kCVPixelBufferOpenGLESCompatibilityKey: CFString](kcvpixelbufferopenglescompatibilitykey.md)
  A key to a Boolean value that indicates whether the pixel buffer is compatible with OpenGL ES contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfacepurgeablekey)*