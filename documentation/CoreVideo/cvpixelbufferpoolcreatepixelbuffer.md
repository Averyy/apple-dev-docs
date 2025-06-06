# CVPixelBufferPoolCreatePixelBuffer(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a pixel buffer from a pixel buffer pool, using the allocator that you specify.

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
func CVPixelBufferPoolCreatePixelBuffer(_ allocator: CFAllocator?, _ pixelBufferPool: CVPixelBufferPool, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

This function creates a new pixel buffer using the pixel buffer attributes specified during pool creation. This buffer has default attachments as specified in the `pixelBufferAttributes` parameter of [`CVPixelBufferPoolCreate(_:_:_:_:)`](cvpixelbufferpoolcreate(_:_:_:_:).md), using either the [`kCVBufferPropagatedAttachmentsKey`](kcvbufferpropagatedattachmentskey.md) or [`kCVBufferNonPropagatedAttachmentsKey`](kcvbuffernonpropagatedattachmentskey.md) attributes.

## Parameters

- `allocator`: The allocator to use for creating the pixel buffer. Pass   to use the default allocator. See   for additional values you can use.
- `pixelBufferPool`: The pixel buffer pool for creating the new pixel buffer.
- `pixelBufferOut`: On output, the newly created pixel buffer.

## See Also

- [func CVPixelBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn](cvpixelbufferpoolcreate(_:_:_:_:).md)
  Creates a pixel buffer pool using the allocator and attributes that you specify.
- [func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(CFAllocator?, CVPixelBufferPool, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md)
  Creates a new pixel buffer with auxiliary attributes from the pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolcreatepixelbuffer(_:_:_:))*