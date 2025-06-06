# CVMetalTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func

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

#### Return Value

The Core Foundation type identifier for the `CVMetalTextureCacheRef` type.

## See Also

- [func CVMetalTextureCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, CFDictionary?, UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](cvmetaltexturecachecreate(_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVMetalTextureCacheCreateTextureFromImage(CFAllocator?, CVMetalTextureCache, CVImageBuffer, CFDictionary?, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:).md)
  Creates a Core Video Metal texture buffer from an existing image buffer.
- [func CVMetalTextureCacheFlush(CVMetalTextureCache, CVOptionFlags)](cvmetaltexturecacheflush(_:_:).md)
  Manually flushes the contents of the provided texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecachegettypeid())*