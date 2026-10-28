# CVMetalBufferCache

**Framework**: Core Video  
**Kind**: class  
**Role**: Class

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

```c
typedef struct __CVMetalBufferCache * CVMetalBufferCacheRef;
```

## Overview

A Core Video Metal buffer cache creates and manages [`CVMetalBuffer`](./cvmetalbuffer.md) buffers. You use a Metal buffer cache to directly read from or write to GPU-based Core Video image buffers in rendering, or for sharing data with Metal kernels.

## Topics

### Functions
- [func CVMetalBufferCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn](./cvmetalbuffercachecreate%28_,_,_,_%29.md)
- [func CVMetalBufferCacheCreateBufferFromImage(CFAllocator?, CVMetalBufferCache, CVImageBuffer, UnsafeMutablePointer<CVMetalBuffer?>) -> CVReturn](./cvmetalbuffercachecreatebufferfromimage%28_,_,_,_%29.md)
- [func CVMetalBufferCacheFlush(CVMetalBufferCache, CVOptionFlags)](./cvmetalbuffercacheflush%28_,_%29.md)
- [func CVMetalBufferCacheGetTypeID() -> CFTypeID](./cvmetalbuffercachegettypeid%28%29.md)
- [func CVMetalBufferGetBuffer(CVMetalBuffer) -> (any MTLBuffer)?](./cvmetalbuffergetbuffer%28_%29.md)
- [func CVMetalBufferGetTypeID() -> CFTypeID](./cvmetalbuffergettypeid%28%29.md)
### Data Types
- [typealias CVMetalBuffer](./cvmetalbuffer.md)
### Constants
- [let kCVMetalBufferCacheMaximumBufferAgeKey: CFString](./kcvmetalbuffercachemaximumbufferagekey.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Metal
- [CVMetalTextureCache](./cvmetaltexturecache-q3j.md)
  A cache used to create and manage Metal texture objects.
- [CVMetalTexture](./cvmetaltexture-q3g.md)
  A texture-based image buffer that supplies source image data for use with the Metal framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercache)*