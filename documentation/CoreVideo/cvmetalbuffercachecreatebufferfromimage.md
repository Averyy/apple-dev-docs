# CVMetalBufferCacheCreateBufferFromImage(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

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

#### Discussion

```None
@function   CVMetalBufferCacheCreateBuffer
@abstract   Creates a CVMetalBuffer object from an existing CVImageBuffer
@param      allocator The CFAllocatorRef to use for allocating the CVMetalBuffer object. May be NULL.
@param      bufferCache The buffer cache object that will manage the buffer.
@param      buffer The CVImageBuffer that you want to create a CVMetalBuffer from.
@param      bufferOut The newly created buffer object will be placed here.
@result     Returns kCVReturnSuccess on success
@discussion Creates or returns a cached CVMetalBuffer object mapped to the CVImageBuffer.
            This creates a live binding between the CVImageBuffer and underlying CVMetalBuffer buffer object.

            IMPORTANT NOTE: Clients should retain CVMetalBuffer objects until they are done using the images in them.
            Retaining a CVMetalBuffer is your way to indicate that you're still using the image in the buffer, and that it should not be recycled yet.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachecreatebufferfromimage(_:_:_:_:))*