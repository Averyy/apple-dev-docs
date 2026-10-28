# CVMetalBufferGetBuffer(_:)

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
func CVMetalBufferGetBuffer(_ buffer: CVMetalBuffer) -> (any MTLBuffer)?
```

```c
extern id<MTLBuffer>CVMetalBufferGetBuffer(CVMetalBufferRef buffer);
```

## Return Value

Metal buffer

## Discussion

Returns the Metal MTLBuffer object of the CVMetalBufferRef

## Parameters

- `buffer`: Target CVMetalBuffer

## See Also

### Functions
- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](./cvmetalbuffercachecreate%28_,_,_,_%29.md)
- [func CVMetalBufferCacheCreateBufferFromImage(CFAllocator?, CVMetalBufferCache, CVImageBuffer, UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn](./cvmetalbuffercachecreatebufferfromimage%28_,_,_,_%29.md)
- [func CVMetalBufferCacheFlush(CVMetalBufferCache, CVOptionFlags)](./cvmetalbuffercacheflush%28_,_%29.md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](./cvmetalbuffercachegettypeid%28%29.md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](./cvmetalbuffergettypeid%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffergetbuffer(_:))*