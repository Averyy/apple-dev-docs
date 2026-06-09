# CVMetalBufferCache

**Framework**: Core Video  
**Kind**: class

A cache used to create and manage Metal buffer objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CVMetalBufferCache
```

#### Overview

A Core Video Metal buffer cache creates and manages [`CVMetalBuffer`](cvmetalbuffer.md) buffers. You use a Metal buffer cache to directly read from or write to GPU-based Core Video image buffers in rendering, or for sharing data with Metal kernels.

## Topics

### Functions
- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](cvmetalbuffercachecreate(_:_:_:_:).md)
- [func CVMetalBufferCacheCreateBufferFromImage(CFAllocator?, CVMetalBufferCache, CVImageBuffer, UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn](cvmetalbuffercachecreatebufferfromimage(_:_:_:_:).md)
- [func CVMetalBufferCacheFlush(CVMetalBufferCache, CVOptionFlags)](cvmetalbuffercacheflush(_:_:).md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](cvmetalbuffercachegettypeid().md)
- [func CVMetalBufferGetBuffer(CVMetalBuffer) -> (any MTLBuffer)?](cvmetalbuffergetbuffer(_:).md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](cvmetalbuffergettypeid().md)
### Data Types
- [typealias CVMetalBuffer](cvmetalbuffer.md)
### Constants
- [let kCVMetalBufferCacheMaximumBufferAgeKey: CFString](kcvmetalbuffercachemaximumbufferagekey.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [CVMetalTextureCache](cvmetaltexturecache-q3j.md)
  A cache used to create and manage Metal texture objects.
- [CVMetalTexture](cvmetaltexture-q3g.md)
  A texture-based image buffer that supplies source image data for use with the Metal framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercache)*