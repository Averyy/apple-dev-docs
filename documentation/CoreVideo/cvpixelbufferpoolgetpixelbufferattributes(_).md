# CVPixelBufferPoolGetPixelBufferAttributes(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

The attributes of pixel buffers which the system creates using the pool you specify.

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
func CVPixelBufferPoolGetPixelBufferAttributes(_ pool: CVPixelBufferPool) -> CFDictionary?
```

```c
extern CFDictionaryRefCVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPoolRef pool);
```

#### Return Value

A Core Foundation dictionary containing the pool attributes, or [`nil`](../ObjectiveC/nil-227m0.md) if the function fails.

#### Discussion

Use this function to obtain information about the pixel buffers which the system creates using the pool you specify, before the system creates those pixel buffers.

## Parameters

- `pool`: The pixel buffer pool that contains the attributes to retrieve.

## See Also

### Inspecting pools
- [func CVPixelBufferPoolGetAttributes(CVPixelBufferPool) -> CFDictionary?](./cvpixelbufferpoolgetattributes%28_%29.md)
  The pool attributes dictionary for a pixel buffer pool.
- [func CVPixelBufferPoolGetTypeID() -> CFTypeID](./cvpixelbufferpoolgettypeid%28%29.md)
  Returns the Core Foundation type identifier of the pixel buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolgetpixelbufferattributes(_:))*