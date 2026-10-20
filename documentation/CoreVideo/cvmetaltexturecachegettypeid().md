# CVMetalTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier for a Core Video Metal texture cache.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureCacheGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVMetalTextureCacheGetTypeID();
```

#### Return Value

The Core Foundation type identifier for the `CVMetalTextureCacheRef` type.

## See Also

### Functions
- [func CVMetalTextureCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, CFDictionary?, UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](./cvmetaltexturecachecreate%28_,_,_,_,_%29.md)
  Creates a new texture cache.
- [func CVMetalTextureCacheCreateTextureFromImage(CFAllocator?, CVMetalTextureCache, CVImageBuffer, CFDictionary?, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](./cvmetaltexturecachecreatetexturefromimage%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a Core Video Metal texture buffer from an existing image buffer.
- [func CVMetalTextureCacheFlush(CVMetalTextureCache, CVOptionFlags)](./cvmetaltexturecacheflush%28_,_%29.md)
  Manually flushes the contents of the provided texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecachegettypeid())*