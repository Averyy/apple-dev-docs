# CVMetalBufferCacheFlush(_:_:)

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
func CVMetalBufferCacheFlush(_ bufferCache: CVMetalBufferCache, _ options: CVOptionFlags)
```

```c
extern void CVMetalBufferCacheFlush(CVMetalBufferCacheRef bufferCache, CVOptionFlags options);
```

## Discussion

Performs internal housekeeping/recycling operations

This call must be made periodically to give the buffer cache a chance to do internal housekeeping operations.

## Parameters

- `bufferCache`: The buffer cache object to flush
- `options`: Currently unused, set to 0.

## See Also

### Functions
- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](./cvmetalbuffercachecreate%28_,_,_,_%29.md)
- [func CVMetalBufferCacheCreateBufferFromImage(CFAllocator?, CVMetalBufferCache, CVImageBuffer, UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn](./cvmetalbuffercachecreatebufferfromimage%28_,_,_,_%29.md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](./cvmetalbuffercachegettypeid%28%29.md)
- [func CVMetalBufferGetBuffer(CVMetalBuffer) -> (any MTLBuffer)?](./cvmetalbuffergetbuffer%28_%29.md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](./cvmetalbuffergettypeid%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercacheflush(_:_:))*