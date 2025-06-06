# CVPixelBufferPoolGetTypeID()

**Framework**: Core Video  
**Kind**: func

Returns the Core Foundation type identifier of the pixel buffer pool type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVPixelBufferPoolGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation type identifier for this pixel buffer.

## See Also

- [func CVPixelBufferPoolGetAttributes(CVPixelBufferPool) -> CFDictionary?](cvpixelbufferpoolgetattributes(_:).md)
  The pool attributes dictionary for a pixel buffer pool.
- [func CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool) -> CFDictionary?](cvpixelbufferpoolgetpixelbufferattributes(_:).md)
  The attributes of pixel buffers which the system creates using the pool you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolgettypeid())*