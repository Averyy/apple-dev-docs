# CVMetalTextureCache

**Framework**: Core Video

A cache used to create and manage Metal texture objects.

#### Overview

A Core Video Metal texture cache creates and manages [`CVMetalTexture`](cvmetaltexture.md) textures. You use a [`CVMetalTextureCache`](cvmetaltexturecache-q3j.md) object to directly read from or write to GPU-based Core Video image buffers in rendering, or for sharing data with Metal kernels. For example, you can use a Metal texture cache to present live output from a device’s camera in a 3D scene rendered with Metal.

## Topics

### Functions
- [func CVMetalTextureCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, CFDictionary?, UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](cvmetaltexturecachecreate(_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVMetalTextureCacheCreateTextureFromImage(CFAllocator?, CVMetalTextureCache, CVImageBuffer, CFDictionary?, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:).md)
  Creates a Core Video Metal texture buffer from an existing image buffer.
- [func CVMetalTextureCacheFlush(CVMetalTextureCache, CVOptionFlags)](cvmetaltexturecacheflush(_:_:).md)
  Manually flushes the contents of the provided texture cache.
- [func CVMetalTextureCacheGetTypeID() -> CFTypeID](cvmetaltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video Metal texture cache.
### Data Types
- [class CVMetalTextureCache](cvmetaltexturecache.md)
  A reference to a Core Video Metal texture cache.
### Constants
- [Cache Attributes](cvmetaltexturecache-cache-attributes.md)
  Attributes specifying texture cache behavior, used with the [`CVMetalTextureCacheCreate(_:_:_:_:_:)`](cvmetaltexturecachecreate(_:_:_:_:_:).md) function.
### Related Documentation
- [Setting up a command structure](../Metal/setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.

## See Also

- [CVMetalTexture](cvmetaltexture-q3g.md)
  A texture-based image buffer that supplies source image data for use with the Metal framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecache-q3j)*