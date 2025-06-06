# CVPixelBufferCreateWithBytes(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a pixel buffer for a given size and pixel format containing data specified by a memory location.

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
func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutableRawPointer, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback?, _ releaseRefCon: UnsafeMutableRawPointer?, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

Some of the parameters specified in this call override equivalent pixel buffer attributes. For example, if you define the `kCVPixelBufferWidth` and `kCVPixelBufferHeight` keys in the pixel buffer attributes parameter (`pixelBufferAttributes`), these values are overridden by the `width` and `height` parameters.

## Parameters

- `allocator`: The allocator to use for creating the buffer pool. Pass   for the   parameter to use the default allocator. See   for additional values you can use.
- `width`: The width of the pixel buffer, in pixels.
- `height`: The height of the pixel buffer, in pixels.
- `pixelFormatType`: The pixel format identified by its respective four character code (type  ).
- `baseAddress`: A pointer to the base address of the memory storing the pixels.
- `bytesPerRow`: The row bytes of the pixel storage memory.
- `releaseCallback`: The callback function to be called when the pixel buffer is destroyed. This callback allows the owner of the pixels to free the memory. See   for more information.
- `releaseRefCon`: The user data identifying the pixel buffer. This value is passed to your pixel buffer release callback.
- `pixelBufferAttributes`: A Core Foundation dictionary with additional attributes for a pixel buffer. This parameter is optional. See   for more details.
- `pixelBufferOut`: On output, the newly created pixel buffer. Ownership follows the  .

## See Also

- [func CVPixelBufferCreate(CFAllocator?, Int, Int, OSType, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreate(_:_:_:_:_:_:).md)
  Creates a single pixel buffer for a given size and pixel format.
- [func CVPixelBufferCreateWithPlanarBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a single pixel buffer in planar format for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithIOSurface(CFAllocator?, IOSurfaceRef, CFDictionary?, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn](cvpixelbuffercreatewithiosurface(_:_:_:_:).md)
  Creates a single pixel buffer for the IO surface that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:))*