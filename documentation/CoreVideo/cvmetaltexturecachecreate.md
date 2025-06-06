# CVMetalTextureCacheCreate(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new texture cache.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ metalDevice: any MTLDevice, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn
```

#### Return Value

Upon successful creation of the texture cache, this function returns [`kCVReturnSuccess`](kcvreturnsuccess.md).

## Parameters

- `allocator`: The memory allocator for the texture.
- `cacheAttributes`: A dictionary specifying options for the cache’s behavior, or   to use default options. For applicable keys and values, see  .
- `metalDevice`: The Metal device used to create texture objects.
- `textureAttributes`: A dictionary specifying options for creating textures from the cache, or   to use default options.
- `cacheOut`: Upon return, contains the newly created texture cache. When this value is  , an error occurred in texture creation.

## See Also

- [func CVMetalTextureCacheCreateTextureFromImage(CFAllocator?, CVMetalTextureCache, CVImageBuffer, CFDictionary?, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:).md)
  Creates a Core Video Metal texture buffer from an existing image buffer.
- [func CVMetalTextureCacheFlush(CVMetalTextureCache, CVOptionFlags)](cvmetaltexturecacheflush(_:_:).md)
  Manually flushes the contents of the provided texture cache.
- [func CVMetalTextureCacheGetTypeID() -> CFTypeID](cvmetaltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video Metal texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecachecreate(_:_:_:_:_:))*