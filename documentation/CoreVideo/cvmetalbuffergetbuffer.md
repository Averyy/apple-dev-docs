# CVMetalBufferGetBuffer(_:)

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
func CVMetalBufferGetBuffer(_ buffer: CVMetalBuffer) -> (any MTLBuffer)?
```

#### Return Value

Metal buffer

#### Discussion

Returns the Metal MTLBuffer object of the CVMetalBufferRef

## Parameters

- `buffer`: Target CVMetalBuffer

## See Also

- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](cvmetalbuffercachecreate(_:_:_:_:).md)
- [func CVMetalBufferCacheCreateBufferFromImage(CFAllocator?, CVMetalBufferCache, CVImageBuffer, UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn](cvmetalbuffercachecreatebufferfromimage(_:_:_:_:).md)
- [func CVMetalBufferCacheFlush(CVMetalBufferCache, CVOptionFlags)](cvmetalbuffercacheflush(_:_:).md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](cvmetalbuffercachegettypeid().md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](cvmetalbuffergettypeid().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffergetbuffer(_:))*