# CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new pixel buffer with auxiliary attributes from the pool.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_ allocator: CFAllocator?, _ pixelBufferPool: CVPixelBufferPool, _ auxAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

This function creates a new [`CVPixelBuffer`](cvpixelbuffer.md) object using the pixel buffer attributes specified during pool creation and the attributes specified in the `auxAttributes` parameter.

## Parameters

- `allocator`: The allocator to use for creating the buffer pool. Pass   to use the default allocator. See   for additional values you can use.
- `pixelBufferPool`: The pixel buffer pool for creating the new pixel buffer.
- `auxAttributes`: An optional dictionary of auxiliary attributes that describes the allocation request. See the Constants topic group below for possible values.
- `pixelBufferOut`: On output, the newly created pixel buffer.

## See Also

- [func CVPixelBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn](cvpixelbufferpoolcreate(_:_:_:_:).md)
  Creates a pixel buffer pool using the allocator and attributes that you specify.
- [func CVPixelBufferPoolCreatePixelBuffer(CFAllocator?, CVPixelBufferPool, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbuffer(_:_:_:).md)
  Creates a pixel buffer from a pixel buffer pool, using the allocator that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:))*