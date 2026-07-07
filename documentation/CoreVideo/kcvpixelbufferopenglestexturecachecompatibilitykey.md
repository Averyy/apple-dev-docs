# kCVPixelBufferOpenGLESTextureCacheCompatibilityKey

**Framework**: Core Video  
**Kind**: var

A key to a Boolean value that indicates whether OpenGL ES performs format conversions of the texture-cache data in a shader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- tvOS 9.0+

## Declaration

```swift
let kCVPixelBufferOpenGLESTextureCacheCompatibilityKey: CFString
```

#### Discussion

This key instructs the graphics subsystem to perform YCbCr-to-RGB conversions for the texture-cache data in a GPU shader, instead of performing them natively in OpenGL ES.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglestexturecachecompatibilitykey)*