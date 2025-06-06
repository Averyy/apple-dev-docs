# CVPixelBufferPoolCreate(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a pixel buffer pool using the allocator and attributes that you specify.

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
func CVPixelBufferPoolCreate(_ allocator: CFAllocator?, _ poolAttributes: CFDictionary?, _ pixelBufferAttributes: CFDictionary?, _ poolOut: UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Result Codes`](result-codes.md) for possible values.

#### Discussion

Use [`CVPixelBufferPoolRelease`](cvpixelbufferpoolrelease.md) to release ownership of the `poolOut` object when you’re done with it.

## Parameters

- `allocator`: The allocator to use for creating the buffer pool. Pass   to use the default allocator. See   for additional values you can use.
- `poolAttributes`: A Core Foundation dictionary that contains the attributes for the pixel buffer pool. See the Constants topic group below for possible values.
- `pixelBufferAttributes`: An optional dictionary that contains the attributes to use to create new pixel buffers within the pool. See   for possible values.
- `poolOut`: On output, the newly created pixel buffer pool.

## See Also

- [func CVPixelBufferPoolCreatePixelBuffer(CFAllocator?, CVPixelBufferPool, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbuffer(_:_:_:).md)
  Creates a pixel buffer from a pixel buffer pool, using the allocator that you specify.
- [func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(CFAllocator?, CVPixelBufferPool, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md)
  Creates a new pixel buffer with auxiliary attributes from the pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolcreate(_:_:_:_:))*