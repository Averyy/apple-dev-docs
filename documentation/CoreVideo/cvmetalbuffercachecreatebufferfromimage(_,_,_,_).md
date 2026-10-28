# CVMetalBufferCacheCreateBufferFromImage(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func CVMetalBufferCacheCreateBufferFromImage(_ allocator: CFAllocator?, _ bufferCache: CVMetalBufferCache, _ imageBuffer: CVImageBuffer, _ bufferOut: UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn
```

```c
extern CVReturn CVMetalBufferCacheCreateBufferFromImage(CFAllocatorRef allocator, CVMetalBufferCacheRef bufferCache, CVImageBufferRef imageBuffer, CVMetalBufferRef*bufferOut);
```

## Return Value

Returns kCVReturnSuccess on success

## Discussion

Creates a CVMetalBuffer object from an existing CVImageBuffer

Creates or returns a cached CVMetalBuffer object mapped to the CVImageBuffer. This creates a live binding between the CVImageBuffer and underlying CVMetalBuffer buffer object.

```
        IMPORTANT NOTE: Clients should retain CVMetalBuffer objects until they are done using the images in them.
        Retaining a CVMetalBuffer is your way to indicate that you're still using the image in the buffer, and that it should not be recycled yet.
```

## Parameters

- `allocator`: The CFAllocatorRef to use for allocating the CVMetalBuffer object. May be NULL.
- `bufferCache`: The buffer cache object that will manage the buffer.
- `bufferOut`: The newly created buffer object will be placed here.

## See Also

### Functions
- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](./cvmetalbuffercachecreate%28_,_,_,_%29.md)
- [func CVMetalBufferCacheFlush(CVMetalBufferCache, CVOptionFlags)](./cvmetalbuffercacheflush%28_,_%29.md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](./cvmetalbuffercachegettypeid%28%29.md)
- [func CVMetalBufferGetBuffer(CVMetalBuffer) -> (any MTLBuffer)?](./cvmetalbuffergetbuffer%28_%29.md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](./cvmetalbuffergettypeid%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachecreatebufferfromimage(_:_:_:_:))*