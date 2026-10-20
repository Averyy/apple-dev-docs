# CVPixelBufferPoolGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

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

```c
extern CFTypeID CVPixelBufferPoolGetTypeID();
```

#### Return Value

The Core Foundation type identifier for this pixel buffer.

## See Also

### Inspecting pools
- [func CVPixelBufferPoolGetAttributes(CVPixelBufferPool) -> CFDictionary?](./cvpixelbufferpoolgetattributes%28_%29.md)
  The pool attributes dictionary for a pixel buffer pool.
- [func CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool) -> CFDictionary?](./cvpixelbufferpoolgetpixelbufferattributes%28_%29.md)
  The attributes of pixel buffers which the system creates using the pool you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolgettypeid())*