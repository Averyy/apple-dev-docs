# kCVReturnPixelBufferNotOpenGLCompatible

**Framework**: Core Video  
**Kind**: var

The pixel buffer is not compatible with OpenGL due to an unsupported buffer size, pixel format, or attribute.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var kCVReturnPixelBufferNotOpenGLCompatible: CVReturn { get }
```

## See Also

- [var kCVReturnInvalidPixelBufferAttributes: CVReturn](kcvreturninvalidpixelbufferattributes.md)
  A buffer cannot be created with the specified attributes.
- [var kCVReturnInvalidPixelFormat: CVReturn](kcvreturninvalidpixelformat.md)
  The buffer does not support the specified pixel format.
- [var kCVReturnInvalidSize: CVReturn](kcvreturninvalidsize.md)
  The buffer cannot support the requested buffer size (usually too big).
- [var kCVReturnPixelBufferNotMetalCompatible: CVReturn](kcvreturnpixelbuffernotmetalcompatible.md)
  The pixel buffer is not compatible with Metal due to an unsupported buffer size, pixel format, or attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvreturnpixelbuffernotopenglcompatible)*