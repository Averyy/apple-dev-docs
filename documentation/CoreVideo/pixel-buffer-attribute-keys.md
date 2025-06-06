# Pixel Buffer Attribute Keys

**Framework**: Core Video

The attributes associated with a pixel buffer.

#### Overview

Use the pixel buffer attribute keys to tell Core Video how to allocate pixel buffers for compatibility with client requirements. A pixel buffer attributes dictionary is a Core Foundation dictionary that contains zero or more key-value pairs. You can pass this dictionary to functions such as [`CVPixelBufferCreate(_:_:_:_:_:_:)`](cvpixelbuffercreate(_:_:_:_:_:_:).md) and [`CVPixelBufferPoolCreate(_:_:_:_:)`](cvpixelbufferpoolcreate(_:_:_:_:).md).

To create an attributes dictionary that’s compatible for multiple clients, pass an array of each client’s attributes dictionary to [`CVPixelBufferCreateResolvedAttributesDictionary(_:_:_:)`](cvpixelbuffercreateresolvedattributesdictionary(_:_:_:).md).

## Topics

### Constants
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
- [let kCVPixelBufferMetalCompatibilityKey: CFString](kcvpixelbuffermetalcompatibilitykey.md)
  A key to a Boolean value that indicates whether the pixel buffer is compatible with the Metal framework.
- [let kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey: CFString](kcvpixelbufferiosurfacecoreanimationcompatibilitykey.md)
  A key to a Boolean value that indicates whether Core Animation can display the pixel buffer.
- [let kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey: CFString](kcvpixelbufferiosurfaceopenglfbocompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL can create a valid texture for use as a color buffer attachment.
- [let kCVPixelBufferIOSurfaceOpenGLESFBOCompatibilityKey: CFString](kcvpixelbufferiosurfaceopenglesfbocompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL ES can create a valid texture for use as a color buffer attachment.
- [let kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey: CFString](kcvpixelbufferiosurfaceopengltexturecompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL can create a valid texture object from the IOSurface-backed pixel buffer.
- [let kCVPixelBufferIOSurfaceOpenGLESTextureCompatibilityKey: CFString](kcvpixelbufferiosurfaceopenglestexturecompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL ES can create a valid texture object from the IOSurface-backed pixel buffer.
- [let kCVPixelBufferOpenGLTextureCacheCompatibilityKey: CFString](kcvpixelbufferopengltexturecachecompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL performs format conversions of the texture-cache data in a shader.
- [let kCVPixelBufferOpenGLESTextureCacheCompatibilityKey: CFString](kcvpixelbufferopenglestexturecachecompatibilitykey.md)
  A key to a Boolean value that indicates whether OpenGL ES performs format conversions of the texture-cache data in a shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/pixel-buffer-attribute-keys)*