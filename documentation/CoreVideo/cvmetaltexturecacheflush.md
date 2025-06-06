# CVMetalTextureCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func

Manually flushes the contents of the provided texture cache.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureCacheFlush(_ textureCache: CVMetalTextureCache, _ options: CVOptionFlags)
```

#### Discussion

Texture caches automatically flush unused resources when you call the [`CVMetalTextureCacheCreateTextureFromImage(_:_:_:_:_:_:_:_:_:)`](cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:).md) function and on the time interval specified by [`kCVMetalTextureCacheMaximumTextureAgeKey`](kcvmetaltexturecachemaximumtextureagekey.md). Use this method when you need fine-grained control over cache contents and memory.

## Parameters

- `textureCache`: The texture cache object to flush.
- `options`: Options for the flush operation. This parameter is currently unused and should be  .

## See Also

- [func CVMetalTextureCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, CFDictionary?, UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](cvmetaltexturecachecreate(_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVMetalTextureCacheCreateTextureFromImage(CFAllocator?, CVMetalTextureCache, CVImageBuffer, CFDictionary?, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:).md)
  Creates a Core Video Metal texture buffer from an existing image buffer.
- [func CVMetalTextureCacheGetTypeID() -> CFTypeID](cvmetaltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video Metal texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecacheflush(_:_:))*