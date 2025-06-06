# CVPixelBufferPoolGetAttributes(_:)

**Framework**: Core Video  
**Kind**: func

The pool attributes dictionary for a pixel buffer pool.

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
func CVPixelBufferPoolGetAttributes(_ pool: CVPixelBufferPool) -> CFDictionary?
```

#### Return Value

A Core Foundation dictionary containing the pool attributes, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the function fails.

## Parameters

- `pool`: The pixel buffer pool that contains the attributes to retrieve.

## See Also

- [func CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool) -> CFDictionary?](cvpixelbufferpoolgetpixelbufferattributes(_:).md)
  The attributes of pixel buffers which the system creates using the pool you specify.
- [func CVPixelBufferPoolGetTypeID() -> CFTypeID](cvpixelbufferpoolgettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolgetattributes(_:))*