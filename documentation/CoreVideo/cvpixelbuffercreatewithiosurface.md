# CVPixelBufferCreateWithIOSurface(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a single pixel buffer for the IO surface that you specify.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVPixelBufferCreateWithIOSurface(_ allocator: CFAllocator?, _ surface: IOSurfaceRef, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

Use [`CVPixelBufferRelease`](cvpixelbufferrelease.md) to release ownership of the `pixelBufferOut` object when you’re done with it.

> ❗ **Important**:  If you are using IOSurface to share CVPixelBuffers between processes and those CVPixelBuffers are allocated via a CVPixelBufferPool, it is important that the CVPixelBufferPool does not reuse CVPixelBuffers whose IOSurfaces are still in use in other processes. CoreVideo and IOSurface will take care of this for if you use IOSurfaceCreateMachPort and IOSurfaceLookupFromMachPort, but NOT if you pass IOSurfaceIDs.

## Parameters

- `allocator`: The allocator to use for creating the buffer pool. Pass   for the   parameter to use the default allocator. See   for additional values you can use.
- `surface`: The IOSurface to use in the pixel buffer.
- `pixelBufferAttributes`: An optional dictionary that contains the attributes for the pixel buffer. See   for possible values.
- `pixelBufferOut`: On output, the newly created pixel buffer.

## See Also

- [func CVPixelBufferCreate(CFAllocator?, Int, Int, OSType, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreate(_:_:_:_:_:_:).md)
  Creates a single pixel buffer for a given size and pixel format.
- [func CVPixelBufferCreateWithBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer, Int, CVPixelBufferReleaseBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md)
  Creates a pixel buffer for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithPlanarBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a single pixel buffer in planar format for a given size and pixel format containing data specified by a memory location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreatewithiosurface(_:_:_:_:))*