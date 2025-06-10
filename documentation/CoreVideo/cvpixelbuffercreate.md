# CVPixelBufferCreate(_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a single pixel buffer for a given size and pixel format.

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
func CVPixelBufferCreate(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

Some of the parameters specified in this function override equivalent pixel buffer attributes. For example, if you set values for the [`kCVPixelBufferWidthKey`](kcvpixelbufferwidthkey.md) and [`kCVPixelBufferHeightKey`](kcvpixelbufferheightkey.md) keys in the `pixelBufferAttributes` dictionary, the values for the `width` and `height` parameters override the values in the dictionary.

Use [`CVPixelBufferRelease`](cvpixelbufferrelease.md) to release ownership of the `pixelBufferOut` object when you’re done with it.

> 💡 **Tip**:  If you need to create and release multiple pixel buffers, use `CVPixelBufferPool` to create a pixel buffer pool that efficiently reuses pixel buffer memory.

## Parameters

- `allocator`: The allocator to use for creating the buffer pool. Pass   for the   parameter to use the default allocator. See   for additional values you can use.
- `width`: The width of the pixel buffer, in pixels.
- `height`: The height of the pixel buffer, in pixels.
- `pixelFormatType`: The pixel format identified by its four-character code.
- `pixelBufferAttributes`: An optional dictionary that contains the attributes for the pixel buffer. See   for possible values.
- `pixelBufferOut`: On output, the newly created pixel buffer.

## See Also

- [func CVPixelBufferCreateWithBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer, Int, CVPixelBufferReleaseBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md)
  Creates a pixel buffer for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithPlanarBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a single pixel buffer in planar format for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithIOSurface(CFAllocator?, IOSurfaceRef, CFDictionary?, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn](cvpixelbuffercreatewithiosurface(_:_:_:_:).md)
  Creates a single pixel buffer for the IO surface that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreate(_:_:_:_:_:_:))*